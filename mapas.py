import json
from pathlib import Path

# Constantes que me van a servir para validar si el mapa está bien definido
ORIENTACIONES = ["NORTE", "ESTE", "SUR", "OESTE"]

# Las flechas para dibujar el recorrido en el mapa
# OJO con la codificación: en Windows se ve mal (estaba usando caracteres unicode)
# 10/10/2026: cambio las flechas a ascii y las defino como constantes para poder dibujar el mapa y la ruta tomada
FLECHAS = {
    "ARRIBA": "^",
    "DERECHA": ">",
    "ABAJO": "v",
    "IZQUIERDA": "<",
}

# Cargamos el mapa especificado
def cargarMapa(mapa):
    carpeta = Path(__file__).parent / "mapas"
    archivo = carpeta / f"{mapa}.json"

    try:
        with open(archivo) as m:
            datos = json.load(m)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return False
    except json.JSONDecodeError as error:
        print(f"Error: No se pudo decodificar el archivo {archivo}. Error: {error}")
        return False

    parametros = ["nombre", "grilla", "inicio", "destino", "tamano_celda_metros", "orientacion_inicial", "maximo_pasos"]

    # Anoche escribí mal los parámetros del mapa 3 y me crasheó el script
    # Tendriamos que verificar si están todos los campos en el mapa antes de cargarlo
    for parametro in parametros:
        if parametro not in datos:
            print(f"Error: El mapa {mapa} no tiene el parámetro {parametro}")
            return False # corto el ciclo

    # Tenemos que validar si el mapa es correcto
    if not validarMapa(datos):
        print(f"Error: El mapa {mapa} no es válido")
        return False

    return {
        "nombre": datos["nombre"],
        "grilla": datos["grilla"],
        "inicio": tuple(datos["inicio"]), # lo paso como tupla para poder operarlo en alGreedy
        "destino": tuple(datos["destino"]),
        "tamano_celda_metros": float(datos["tamano_celda_metros"]),
        "orientacion_inicial": datos["orientacion_inicial"],
        "maximo_pasos": int(datos["maximo_pasos"])
    }

# Ya terminé de testear la función de greedy, con lo que me pasó anoche
# debería validar el menos si el mapa tiene bien los datos, como la orientación inicial (con constantes)
# y los campos de inicio, destino, pasos y tamaño de celda.
# La validación de la grilla creo que debería ser rectangular (mxm), consultar al profe, al menos en los ejemplos es una matriz cuadrada
def validarMapa(mapa):
    # Mejor vamos validando en orden, primero validamos la grilla
    grilla = mapa["grilla"]
    if not isinstance(grilla, list) or not grilla:
        print(f"Error: La grilla debe ser una lista no vacía.")
        return False

    # Validamos que la grilla sea rectangular
    filas = len(grilla)
    if filas == 0:
        print(f"Error: La grilla debe tener al menos una fila.")
        return False

    columnas = len(grilla[0])
    if columnas == 0:
        print(f"Error: La grilla debe tener al menos una columna.")
        return False

    for fila in grilla:
        if not isinstance(fila, list):
            print(f"Error: Cada elemento de la grilla debe ser una lista.")
            return False
        if len(fila) != columnas:
            print(f"Error: Todas las filas de la grilla deben tener la misma cantidad de elementos.")
            return False
        
        for valor in fila:
            if isinstance(valor, bool) or valor not in (0, 1, 2):
                print(f"Error: La grilla tiene un valor inválido ({valor}). Solo se permite 0, 1 o 2.")
                return False

    # Validamos las posiciones de inicio y destino
    inicio = mapa["inicio"]
    destino = mapa["destino"]

    # Validamos que inicio y destino sean listas de dos enteros
    if (not isinstance(inicio, list) or len(inicio) != 2 or not all(isinstance(v, int) and not isinstance(v, bool) for v in inicio)):
        print(f"Error: La posición de inicio debe ser una lista de dos enteros.")
        return False

    if (not isinstance(destino, list) or len(destino) != 2 or not all(isinstance(v, int) and not isinstance(v, bool) for v in destino)):
        print(f"Error: La posición de destino debe ser una lista de dos enteros.")
        return False

    # Validamos que inicio y destino estén dentro de la grilla y en una celda libre
    for nombre, (f, c) in (("inicio", inicio), ("destino", destino)):
        if f < 0 or f >= filas or c < 0 or c >= columnas:
            print(f"Error: La posición de {nombre} {[f, c]} está fuera de la grilla.")
            return False
        if grilla[f][c] != 0:
            print(f"Error: La posición de {nombre} {[f, c]} no es una celda libre.")
            return False

    # Validamos el campo de tamaño de celda
    tamano_celda = mapa["tamano_celda_metros"]
    if not isinstance(tamano_celda, (int, float)) or isinstance(tamano_celda, bool) or tamano_celda <= 0:
        print(f"Error: El valor de tamaño de celda debe ser un número mayor a 0.")
        return False
    
    # Validamos el campo orientacion_inicial (y de paso ya definimos la variable orientacion)
    orientacion = mapa["orientacion_inicial"]

    if orientacion not in ORIENTACIONES:
        print(f"Error: La orientación inicial {orientacion} no es válida.")
        return False

    # Validamos maximo_pasos
    maximo_pasos = mapa["maximo_pasos"]
    if not isinstance(maximo_pasos, int) or isinstance(maximo_pasos, bool) or maximo_pasos <= 0:
        print(f"Error: El valor de máximo de pasos debe ser mayor a 0.")
        return False

    # Si llegamos hasta acá es que el mapa es válido
    return True

# PAra una mejor ayuda visual tendríamos que dibujar el mapa
# Como una matriz tipo un mapa de pacman (adjunto dibujo para que se entienda, perdón)
# 10/10/2026: agrego los parámetros ruta y movimientos para reutilizar la función y dibujar el mapa del recorrido
def dibujarMapa(mapa, ruta = None, movimientos = None):
    grilla = mapa["grilla"]
    caracteres = {
        0: "*",
        1: "#",
        2: "X"
    }

    if ruta:
        print("Referencias: I = inicio | D = destino | F = posición final | # = obstáculo | X = zona prohibida | * = libre | ^ > v < = recorrido")

    # En cada celda de la ruta va la flecha hacia donde salió el robot
    # ruta[k] es donde estaba y movimientos[k] es lo que hizo desde ahí
    flechas = {}
    if ruta and movimientos:
        for k in range(len(movimientos)):
            flechas[ruta[k]] = FLECHAS[movimientos[k]]

    # Si no llegó al destino, marcamos dónde se quedó
    final = None
    if ruta and ruta[-1] != mapa["destino"]:
        final = ruta[-1]

    # Dibujamos la primera fila (columnas)
    # NO olvidarse de que la primera columna está vacía para dibujar el inidce de la fila
    lineas = ["    " + " ".join(str(c) for c in range(len(grilla[0])))] # grilla[0] es la primera fila de la grilla, dibujamos las columnas con la cantidad de elementos
    for i, fila in enumerate(grilla):
        elementos = []
        for j, elemento in enumerate(fila):
            posicion = (i, j)
            if posicion == mapa["inicio"]:
                # El inicio lo dibujamos con una I
                elementos.append("I")
            elif posicion == mapa["destino"]:
                # El destino lo dibujamos con una D
                elementos.append("D")
            elif posicion == final:
                # Donde quedó trabado el robot
                elementos.append("F")
            elif posicion in flechas:
                elementos.append(flechas[posicion])
            else:
                elementos.append(caracteres.get(elemento, "?"))  # Si el elemento no está en el diccionario, dibujamos un ?
        lineas.append(f"{i:2}  " + " ".join(elementos))

    # Imprimimos el mapa
    print("\n".join(lineas))