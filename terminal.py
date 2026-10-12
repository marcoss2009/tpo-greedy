# Importamos la librería OS para acceder a funciones del sistema operativo
# Me robé esta función del código de un TP de Progra 1, perdón pero es útil (https://github.com/marcoss2009/cathedral-software/blob/master/terminal.py)
from os import system, name

def limpiarTerminal():
    # Verifiquemos si estamos en Windows (NT = Windows Kernel)
    if name == "nt":
        system('cls')
    else:
        # Estamos en UNIX, osea, mac, linux, etc.
        system('clear')