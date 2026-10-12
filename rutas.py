from terminal import limpiarTerminal
import mapas
import greedy
import ottoman

criterios = {
    "DESTINO_ALCANZADO": "El robot llegó a la celda destino.",
    "BLOQUEADO": "No existen candidatos válidos para continuar.",
    "LIMITE_DE_PASOS": "Se alcanzó el máximo de pasos permitido."
}

def main():
    # Limpiamos la terminal
    limpiarTerminal()

    print(" Carga de mapa - TP Greedy ".center(80,'-'))

    while True:
        mapa = input("Ingrese el nombre del mapa a cargar: ")

        datos_mapa = mapas.cargarMapa(mapa)
        if datos_mapa:
            print((" " + datos_mapa["nombre"] + " ").center(80,'-'))
            # Mapa cargado correctamente, dibujamos el mapa en la terminal
            # para tener una ayuda visual
            print(" Gráfico de mapa inicial ".center(80,'-'))
            mapas.dibujarMapa(datos_mapa)

            # Ejecutamos el algoritmo greedy
            print(" Algoritmo Greedy ".center(80,'-'))
            ruta, movimientos, fin, pasos = greedy.alGreedy(datos_mapa)
            print("Ruta: ", " -> ".join(f"({f},{c})" for f, c in ruta))
            print("Orientación inicial: ", datos_mapa["orientacion_inicial"])
            print("Tamaño de celda: ", datos_mapa["tamano_celda_metros"], " m")

            # Generamos las instrucciones para Ottoman
            instrucciones = ottoman.generarInstrucciones(movimientos, datos_mapa["orientacion_inicial"], datos_mapa["tamano_celda_metros"])
            print(" Instrucciones: ", " -> ".join(instrucciones))

            print(" Resultados del algoritmo y mapa del recorrido ".center(80,'-'))

            print("Fin del algoritmo: ", fin, "-", criterios[fin])
            print("Número de pasos: ", pasos)

            # Dibujamos el recorrido sobre el mapa
            mapas.dibujarMapa(datos_mapa, ruta, movimientos)

            if fin != "DESTINO_ALCANZADO":
                print(f" ATENCIÓN: el robot no llega al destino, se queda en {ruta[-1]}")
            break
        # else: el error lo imprime cargarMapa

if __name__ == "__main__":
    main()