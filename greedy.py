# Definimos todos los métodos para ejecutar el algoritmo
# TODO: revisar si cumple con los tres mapas, solo lo testeé con el mapa 1
# Críterios de desempate
MOVIMIENTOS = [
    ("ARRIBA", -1, 0), # posición actual (misma columna) en la fila de arriba
    ("DERECHA", 0, 1), # posicion actual + 1 en la misma fila
    ("ABAJO", 1, 0), # posicion actual en la fila de abajo
    ("IZQUIERDA", 0, -1), # posicion actual - 1 en la misma fila
]


# Definimos los criterios de finalización
def alGreedy(mapa):
    # Datos iniciales del mapa
    grilla = mapa["grilla"]
    inicio = mapa["inicio"]
    destino = mapa["destino"]

    # Damos por sentado que ya visitamos el inicio
    posicion = inicio # Posición actual
    visitados = {posicion}
    pasos = 0 # en teoría la posición actual no es un paso (aclaro porque en la hoja puse que eran 9 pasos pero en realidad aparecí de la nada en el inicio)
    ruta = [posicion] # guardamos la ruta que vamos tomando
    movimientos = [] # guardamos el nombre de cada movimiento para imprimir las instrucciones para Ottoman

    while True:
        if posicion == destino:
            fin = "DESTINO_ALCANZADO"
            break # rompo el ciclo

        if pasos >= mapa["maximo_pasos"]:
            fin = "LIMITE_DE_PASOS"
            break # rompo el ciclo

        candidatos = obtenerCandidatos(posicion, mapa, visitados, destino)
        if not candidatos:
            fin = "BLOQUEADO"
            break # rompo el ciclo

        # Seleccionamos el candidato de menor distancia
        candidata, movimiento, distancia = seleccionarCandidato(candidatos)
        pasos += 1
        ruta.append(candidata)
        movimientos.append(movimiento)
        visitados.add(candidata)
        posicion = candidata

    return ruta, movimientos, fin, pasos

# Generamos todos los lugares a los que el robot podría moverse desde donde está
# Nos apoyamos en la definición de MOVIMIENTOS ya que es el orden en el que debe moverse el robot
# Cada MOVIMIENTOS es un desplazamiento (documentado en comentarios al lado de la definición)
def obtenerCandidatos(posicion, mapa, visitados, destino):
    candidatos = []
    for movimiento, d_fila, d_columna in MOVIMIENTOS:
        candidata = (posicion[0] + d_fila, posicion[1] + d_columna)
        if factibilidad(candidata, mapa, visitados):
            distancia = manhattan(candidata, destino)
            candidatos.append((candidata, movimiento, distancia))
    return candidatos

# Determinamos si se puede pisar en esta celda candidata
def factibilidad(candidata, mapa, visitados):
    # Verificamos que la candidata esté dentro de los límites del mapa
    if candidata[0] < 0 or candidata[0] >= len(mapa["grilla"]):
        return False
    if candidata[1] < 0 or candidata[1] >= len(mapa["grilla"][0]):
        return False

    # Si el elemento del mapa no es 0 (zona libre) entonces no puede ser factible
    if mapa["grilla"][candidata[0]][candidata[1]] != 0:
        return False

    # Verificamos que la candidata no haya sido visitada previamente
    if candidata in visitados:
        return False

    # Si llegamos hasta acá entoncés es factible
    return True

# Seleccionamos el candidato con menor distancia
# Con min obtenemos el primero entre los empatados, y como los candidatos vienen en el orden ARRIBA -> DERECHA -> ABAJO -> IZQUIERDA, ese es el desempate.
def seleccionarCandidato(candidatos):
    return min(candidatos, key=lambda candidato: candidato[2])

# Lo mismo que en el PDF del tpo pero indicando los indices
def manhattan(posicion, destino):
    return abs(posicion[0] - destino[0]) + abs(posicion[1] - destino[1])