from chess.pieza import pieza

class Alfil(pieza):
    def __init__(self, color, fila, columna):
        super().__init__('Alfil', color, fila, columna)
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return "♜"
        else:
            return "♖"

    def movimientos_validos(self):
        pass