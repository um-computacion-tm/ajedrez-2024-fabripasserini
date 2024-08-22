from chess.pieza import pieza

class Torre(pieza):
    def __init__(self, color, fila, columna):
        super().__init__('Torre', color, fila, columna)
    
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"

    def __movimientos_validos__(self):
        pass