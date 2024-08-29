class pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return self.blanco_str
        else:
            return self.negro_str