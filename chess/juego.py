from chess.main import Ajedrez
from chess.excepciones import  *
import sys
import os



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



if __name__ == "__main__":
    main()