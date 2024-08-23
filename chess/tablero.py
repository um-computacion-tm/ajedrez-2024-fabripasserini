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
    
    def mover_pieza(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        if not (0 <= desde_fila < 8 and 0 <= desde_columna < 8):
            raise ValueError("Coordenadas de origen fuera del tablero")
        if not (0 <= hasta_fila < 8 and 0 <= hasta_columna < 8):
            raise ValueError("Coordenadas de destino fuera del tablero")

        pieza = self.__casillas__[desde_fila][desde_columna]
        self.__casillas__[desde_fila][desde_columna] = ' '
        self.__casillas__[hasta_fila][hasta_columna] = pieza

if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar_tablero()
