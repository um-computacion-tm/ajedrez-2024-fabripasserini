from chess.main import Ajedrez


def main():
    ajedrez = Ajedrez()
    while ajedrez.en_juego():
        play(ajedrez)


def play(ajedrez):
    try:
        print(ajedrez.mostrar_tablero())
        print("turno: ", ajedrez.turno)
        desde_fila = int(input("desde fila: "))
        desde_columna = int(input("desde columna: "))
        hacia_fila = int(input("hacia fila: "))
        hacia_columna = int(input("hacia columna: "))
        
        ajedrez.mover(
            desde_fila,
            desde_columna,
            hacia_fila,
            hacia_columna,
        )
    except Exception as e:
        print("error", e)



if __name__ == '__main__':
    main()