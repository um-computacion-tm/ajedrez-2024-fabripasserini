from chess.excepciones import *

class Pieza():
    def __init__(self, color,  tablero):
        self.__color__ = color
        self.__tablero__ = tablero
    
    def __str__(self):
        if self.__color__ == "BLANCO":
            return self.blanco_str
        else:
            return self.negro_str
        
    def obtener_color(self):
        return self.__color__
    
    
    def posiciones_validas (self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        posibles_posiciones = self.obtener_posibles_posiciones(desde_fila, desde_columna)
        return (hasta_fila, hasta_columna) in posibles_posiciones
    
    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        # Este método debe ser implementado en las subclases.
        raise NotImplementedError("Este método debe ser implementado en las subclases.")

    
    
    
    
    
  
  