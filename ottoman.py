# Definición de instrucciones para Ottoman
from mapas import ORIENTACIONES

# Cada movimiento de la grilla equivale a mirar hacia un punto cardinal
ORIENTACION_MOVIMIENTO = {
    "ARRIBA": "NORTE",
    "DERECHA": "ESTE",
    "ABAJO": "SUR",
    "IZQUIERDA": "OESTE",
}

def generarInstrucciones(movimientos, orientacion_inicial, tamano_celda):
    instrucciones = []
    # Trabajamos con el índice dentro de ORIENTACIONES para poder restar
    orientacion = ORIENTACIONES.index(orientacion_inicial)

    for movimiento in movimientos:
        nueva = ORIENTACIONES.index(ORIENTACION_MOVIMIENTO[movimiento])
        diferencia = (nueva - orientacion) % 4

        # Si cambia la orientación primero giramos
        if diferencia == 1:
            instrucciones.append("GIRAR DERECHA 90°")
        elif diferencia == 2:
            instrucciones.append("GIRAR 180°")
        elif diferencia == 3:
            instrucciones.append("GIRAR IZQUIERDA 90°")
        orientacion = nueva

        # Cada movimiento es una celda
        instrucciones.append(f"AVANZAR {formatearMetros(tamano_celda)}")

    ## TODO: agregar script compatible con la API de Unitree

    return instrucciones

# Para mostrarlos como en el ejemplo del punto 6 del TPO (AVANZAR 0,50 m)
def formatearMetros(metros):
    return f"{metros:.2f}".replace(".", ",") + " m"