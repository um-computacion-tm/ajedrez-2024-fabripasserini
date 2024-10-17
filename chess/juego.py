from chess.main import Ajedrez
from chess.excepciones import  *



def main():
    chess = Ajedrez()
    menu(chess)


def menu(chess):
    while not chess.__terminar_partida__:
        print("BIENVENIDO"  )
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            print()
            menu_juego(chess)
        elif opcion == "2":
            chess.terminar_partida()
            break
        else:
            print("Opción no válida")


def menu_juego(chess):
    while not chess.__terminar_partida__:
        print("------------------------------------------------------------------------")
        print("Menú de juego")
        print("Turno: ", chess.turnos())
        print()
        print("1. Mover pieza")
        print("2. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            play(chess)
        elif opcion == "2":
            print()
            chess.terminar_partida()
            break
       
        

def play(chess):
    try:
        print()
        chess.mostrar_tablero()  
        print("Turno: ", chess.turnos())  
        desde_fila = int(input("Desde fila: "))
        desde_columna = int(input("Desde columna: "))
        hasta_fila = int(input("Hasta fila: "))
        hasta_columna = int(input("Hasta columna: "))

        print(f"movimiento seleccionado Desde ({desde_fila}, {desde_columna}) hasta ({hasta_fila}, {hasta_columna})")
        chess.mover_pieza(desde_fila, desde_columna, hasta_fila, hasta_columna)
        chess.mostrar_tablero()  

    except movimiento_inválido as e:
        print(f"Invalid move: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()