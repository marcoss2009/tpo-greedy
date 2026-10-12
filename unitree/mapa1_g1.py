# Script generado por unitree.py a partir de las instrucciones de ottoman.py
# Instrucciones: AVANZAR 0,50 m -> AVANZAR 0,50 m -> GIRAR DERECHA 90° -> AVANZAR 0,50 m -> AVANZAR 0,50 m -> GIRAR IZQUIERDA 90° -> AVANZAR 0,50 m -> AVANZAR 0,50 m -> GIRAR DERECHA 90° -> AVANZAR 0,50 m -> AVANZAR 0,50 m
from g1_student_api import RobotG1

def mueveRobot(robot):
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # GIRAR DERECHA 90°
    robot.movimiento(adelante=0.0, costado=0.0, giro=-0.5, tiempo=3.1416)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # GIRAR IZQUIERDA 90°
    robot.movimiento(adelante=0.0, costado=0.0, giro=0.5, tiempo=3.1416)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # GIRAR DERECHA 90°
    robot.movimiento(adelante=0.0, costado=0.0, giro=-0.5, tiempo=3.1416)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)
    # AVANZAR 0,50 m
    robot.movimiento(adelante=0.25, costado=0.0, giro=0.0, tiempo=2.0)

def main():
    robot = RobotG1()
    robot.conectar()
    try:
        mueveRobot(robot)
    finally:
        # Pase lo que pase frenamos al robot
        robot.detenerse()
        robot.desconectar()

if __name__ == "__main__":
    main()
