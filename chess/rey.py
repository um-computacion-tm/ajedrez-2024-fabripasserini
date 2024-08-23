from chess.pieza import pieza

class Rey(pieza):
    def __init__(self, color, fila, columna):
        super().__init__('Rey', color, fila, columna)
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return "♜"
        else:
            return "♖"

    def movimientos_validos(self):
        pass