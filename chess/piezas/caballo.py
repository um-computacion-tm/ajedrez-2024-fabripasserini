from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Caballo(Pieza):
    blanco_str = "♞"
    negro_str = "♘"

    def __init__(self, color, nombre, tablero):
        super().__init__(color, nombre, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        # Devuelve todas las posiciones posibles a las que el caballo puede moverse
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles
    
    def es_casilla_vacia(self, fila, columna): # Verifica si una casilla está vacía en el tablero.
        return self.__tablero__.obtener_pieza(fila, columna) is None
    
    def es_posicion_valida(self, fila, columna): # Verifica si la posición está dentro de los límites del tablero.
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True
    
    def obtener_posiciones_mover(self, desde_fila, desde_columna): # Devuelve las posiciones válidas a las que el caballo puede moverse (movimiento en L)
        posiciones = []
        movimientos = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),  
            (1, 2), (1, -2), (-1, 2), (-1, -2)   
        ]
        
        for movimiento in movimientos:
            nueva_fila = desde_fila + movimiento[0]
            nueva_columna = desde_columna + movimiento[1]
            
            if self.es_posicion_valida(nueva_fila, nueva_columna):
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
                if otra_pieza is None:  
                    posiciones.append((nueva_fila, nueva_columna))
                elif otra_pieza.__color__ != self.__color__:  
                    posiciones.append((nueva_fila, nueva_columna))
                else:
                    raise movimiento_inválido(f"No puedes mover el caballo a una casilla ocupada por tu propia pieza en ({nueva_fila}, {nueva_columna}).")
        
        return posiciones