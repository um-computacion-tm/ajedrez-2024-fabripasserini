from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Caballo(Pieza):
    blanco_str = "♞"
    negro_str = "♘"

    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Devuelve todas las posiciones posibles a las que el caballo puede moverse.
        """
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles
    
    def es_casilla_vacia(self, fila, columna):
        """
        Verifica si una casilla está vacía en el tablero.
        """
        return self.__tablero__.obtener_pieza(fila, columna) is None
    
    def es_posicion_valida(self, fila, columna):
        """
        Verifica si la posición está dentro de los límites del tablero.
        """
        return 0 <= fila < 8 and 0 <= columna < 8
    
    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones válidas a las que el caballo puede moverse (movimiento en 'L').
        """
        posiciones = []
        movimientos = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),  
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for movimiento in movimientos:
            nueva_fila = desde_fila + movimiento[0]
            nueva_columna = desde_columna + movimiento[1]
            
            if not self.es_posicion_valida(nueva_fila, nueva_columna):
                continue  # Saltamos movimientos fuera del tablero

            otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)

            if otra_pieza is None:  # Si la casilla está vacía, el caballo puede moverse
                posiciones.append((nueva_fila, nueva_columna))
            elif otra_pieza.__color__ != self.__color__:  # Si la pieza es enemiga, puede capturarla
                posiciones.append((nueva_fila, nueva_columna))

        return posiciones
