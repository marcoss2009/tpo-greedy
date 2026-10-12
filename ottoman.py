# Definición de instrucciones para Ottoman
from mapas import ORIENTACIONES
import unitree

# Cada movimiento de la grilla equivale a mirar hacia un punto cardinal
ORIENTACION_MOVIMIENTO = {
    "ARRIBA": "NORTE",
    "DERECHA": "ESTE",
    "ABAJO": "SUR",
    "IZQUIERDA": "OESTE",
}

def generarInstrucciones(movimientos, orientacion_inicial, tamano_celda, nombre_script=None):
    instrucciones = []
    comandos = [] # las mismas instrucciones pero como datos, para el script de Unitree

    # Trabajamos con el índice dentro de ORIENTACIONES para poder restar
    orientacion = ORIENTACIONES.index(orientacion_inicial)

    for movimiento in movimientos:
        nueva = ORIENTACIONES.index(ORIENTACION_MOVIMIENTO[movimiento])
        diferencia = (nueva - orientacion) % 4

        # Si cambia la orientación primero giramos
        if diferencia == 1:
            instrucciones.append("GIRAR DERECHA 90°")
            comandos.append(("GIRAR", -90))
        elif diferencia == 2:
            instrucciones.append("GIRAR 180°")
            comandos.append(("GIRAR", 180))
        elif diferencia == 3:
            instrucciones.append("GIRAR IZQUIERDA 90°")
            comandos.append(("GIRAR", 90))
        orientacion = nueva

        # Cada movimiento es una celda
        instrucciones.append(f"AVANZAR {formatearMetros(tamano_celda)}")
        comandos.append(("AVANZAR", tamano_celda))

    # Si nos pasan un nombre, generamos el script para el simulador de Unitree
    if nombre_script:
        archivo = unitree.generarScriptUnitree(instrucciones, comandos, nombre_script)
        print(f"Script para Unitree generado en: {archivo}")

    return instrucciones

# Para mostrarlos como en el ejemplo del punto 6 del TPO (AVANZAR 0,50 m)
def formatearMetros(metros):
    return f"{metros:.2f}".replace(".", ",") + " m"