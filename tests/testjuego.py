from chess.main import Ajedrez


def main():
    ajedrez = Ajedrez()
    while ajedrez.en_juego():
        jugar(ajedrez)


def jugar(ajedrez):
    try:
        print(ajedrez.mostrar_tablero())
        print("turn: ", ajedrez.turno)
        desde_fila = int(input("From fila: "))
        desde_columna = int(input("From columna: "))
        hacia_fila = int(input("hacia fila: "))
        hacia_columna = int(input("hacia columna: "))
        # :)
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