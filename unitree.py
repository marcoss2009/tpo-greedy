# Este punto excede a las consignas del TPO pero no me parece que esté demás para
# testear en el simulador de Unitree como se comporta el robot con las intrucciones
# generadas desde ottoman.py; para esto vamos a "traducir" las instrucciones
# generadas en el archivo mencionado a un script compatible con la API de Unitree.
# Como API base voy a usar el ejemplo publicado en el repo del robot del UADE:
# https://github.com/tsamaan/UadeRobotLab/blob/main/04Simuladores/UnitreeMujocoOficial/examples/alumnos_g1_api.py

import math
from pathlib import Path

# La API trabaja con velocidad y tiempo: distancia = velocidad x tiempo
# el simulador recorta adelante a 0.45 m/s, giro a 1.0 rad/s y tiempo a 10 s
VELOCIDAD_AVANCE = 0.25 # m/s
VELOCIDAD_GIRO = 0.5 # rad/s (positivo = izquierda, negativo = derecha)

CARPETA_SCRIPTS = Path(__file__).parent / "unitree"

# Convierte un comando de ottoman en los parámetros de robot.movimiento()
def traducirComando(comando):
    tipo, valor = comando
    if tipo == "AVANZAR":
        # valor = metros
        tiempo = valor / VELOCIDAD_AVANCE
        return VELOCIDAD_AVANCE, 0.0, round(tiempo, 4)
    # tipo == "GIRAR", valor = grados (positivo = izquierda, negativo = derecha)
    giro = VELOCIDAD_GIRO if valor > 0 else -VELOCIDAD_GIRO
    tiempo = math.radians(abs(valor)) / VELOCIDAD_GIRO
    return 0.0, giro, round(tiempo, 4)

def generarScriptUnitree(instrucciones, comandos, nombre_script):
    lineas = [
        "# Script generado por unitree.py a partir de las instrucciones de ottoman.py",
        f"# Instrucciones: {' -> '.join(instrucciones)}",
        "from g1_student_api import RobotG1",
        "",
        "def mueveRobot(robot):",
    ]

    # Una llamada a movimiento() por instrucción, con la instrucción como comentario
    for instruccion, comando in zip(instrucciones, comandos):
        adelante, giro, tiempo = traducirComando(comando)
        lineas.append(f"    # {instruccion}")
        lineas.append(f"    robot.movimiento(adelante={adelante}, costado=0.0, giro={giro}, tiempo={tiempo})")

    if not comandos:
        lineas.append("    pass # no hay movimientos")

    lineas += [
        "",
        "def main():",
        "    robot = RobotG1()",
        "    robot.conectar()",
        "    try:",
        "        mueveRobot(robot)",
        "    finally:",
        "        # Pase lo que pase frenamos al robot",
        "        robot.detenerse()",
        "        robot.desconectar()",
        "",
        "if __name__ == \"__main__\":",
        "    main()",
    ]

    CARPETA_SCRIPTS.mkdir(exist_ok=True)
    archivo = CARPETA_SCRIPTS / f"{nombre_script}_g1.py"
    archivo.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return archivo