class Tablero:
    def __init__(self):
        self.__casillas__ = [[' ' for _ in range(8)] for _ in range(8)]
        self.inicializar_tablero()

    def inicializar_tablero(self):
        self.__casillas__[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        self.__casillas__[1] = ['♟' for _ in range(8)]
        self.__casillas__[6] = ['♙' for _ in range(8)]
        self.__casillas__[7] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']

    def mostrar_tablero(self):
        print("   0  1  2  3  4  5  6  7")
        print(" +-------------------------+")
        for i, fila in enumerate(self.__casillas__):
            print(f"{0+i}| " + " ".join(f"{casilla:2}" for casilla in fila) + " |")
        print(" +-------------------------+")
    

if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar_tablero()   


    