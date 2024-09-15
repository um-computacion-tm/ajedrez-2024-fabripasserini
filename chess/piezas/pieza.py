class Pieza:
    def __init__(self, color, tablero):
        self.__color__ = color
        self.__tablero__ = tablero
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return self.blanco_str
        else:
            return self.negro_str
    
    def posiciones_validas (self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        posibles_posiciones = self.obtener_posibles_posiciones(desde_fila, desde_columna)
        return posibles_posiciones (hasta_fila, hasta_columna) in posibles_posiciones
    
    def posibles_posiciones_vd(self, fila, columna):
        posibles = []
        for siguente_fila in range(fila + 1, 8):
            otra_pieza = self.__tablero__.obtener_pieza(siguente_fila, columna)
            if otra_pieza is not None:
                if otra_pieza.__color__ != self.__color__:
                    posibles.append((siguente_fila, columna))
                break
            posibles.append((siguente_fila, columna))
        return posibles
    
    def obtener_color(self):
        return self.__color__