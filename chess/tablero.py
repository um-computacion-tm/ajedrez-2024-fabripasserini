class Tablero:
    def __init__(self):
        self.__casillas__ = [[' ' for _ in range(8)] for _ in range(8)]
        self.inicializar_tablero()

    def inicializar_tablero(self):
        self.__casillas__[0] = ['T', 'C', 'A', 'D', 'R', 'A', 'C', 'T']
        self.__casillas__[1] = ['P' for _ in range(8)]
        self.__casillas__[6] = ['P' for _ in range(8)]
        self.__casillas__[7] = ['T', 'C', 'A', 'D', 'R', 'A', 'C', 'T']

    def mostrar_tablero(self):
        print("  a b c d e f g h")
        print(" +-------------------------+")
        for i, fila in enumerate(self.__casillas__):
            print(f"{8-i}| " + " ".join(f"{casilla:2}" for casilla in fila) + " |")
        print(" +-------------------------+")
    

if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar_tablero()   


    