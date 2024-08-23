from chess.pieza import pieza

class Caballo(pieza):
    def __init__(self, color, fila, columna):
        super().__init__('Caballo', color, fila, columna)
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return "♜"
        else:
            return "♖"

    def movimientos_validos(self):
        pass