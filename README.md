# TP 03 · Planificador de Rutas con Estrategia Greedy
Repositorio del Trabajo Práctico de la materia **Programación III** del segundo cuatrimestre de 2026.

Profesor: Ferrare, Rodrigo Mariano

## Integrantes del grupo
|Nombre del alumno|Legajo|
|--|--|
|Diaz, Claudino|1185188|
|Dumañski, Melina|1135912|
|Muñoz, Marcos|1196001|

## Objetivo del trabajo
Implementar en Python un planificador de movimientos para el robot Unitree utilizando una estrategia greedy. El objetivo es observar cómo una decisión localmente conveniente puede producir una buena ruta, una ruta no óptima o incluso un bloqueo aunque el mapa posea solución.

## Inicialización
El proyecto debe inicializarse desde el archivo `tp_greedy_munoz.py`.

    $ python3 tp_greedy_munoz.py

## Ejecución en robot de Unitree
Si bien el TPO no lo pide explícitamente en los puntos de entrega hemos decidido crear un nuevo módulo llamado `unitree.py` para crear un script ya listo para correr en el simulador de Unitree proporcionado en la primera página del TPO. Para esto, hemos tomado como base la API de ejemplo documentada en el archivo `g1_student_api.py` que hemos clonado al directorio `unitee/` donde tambien almacenamos los scripts generados cada vez que corremos un mapa.

La forma para correrlo es la siguiente: abrimos una terminal para cargar el emulador (siguiendo las instrucciones del reposito oficial, en caso de utilizar Mac tenemos que usar la siguiente documentación: https://github.com/marcoss2009/uade-robot-lab) y en otra terminal nos paramos en la carpeta del proyecto y ejecutamos el script correspondiente al mapa que se quiere simular, en este caso, vamos a ejemplificar con el mapa 1:

    $ python3 unitree/mapa1_g1.py