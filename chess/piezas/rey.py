from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Rey(Pieza):
    blanco_str = "♚"
    negro_str = "♔"

    def __init__(self, color, tablero):
        super().__init__(color, tablero)


    def obtener_posibles_posiciones(self, desde_fila, desde_columna): # Devuelve todas las posiciones posibles a las que el rey puede moverse
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles

    def es_casilla_vacia(self, fila, columna): # Verifica si una casilla está vacía en el tablero.
        return self.__tablero__.obtener_pieza(fila, columna) is None
    
    def es_posicion_valida(self, fila, columna): # Verifica si la posición está dentro de los límites del tablero.
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True

    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        posiciones = []
        direcciones = [
        (-1, 0), (1, 0), (0, -1), (0, 1), 
        (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
    
        for direccion in direcciones:
            nueva_fila = desde_fila + direccion[0]
            nueva_columna = desde_columna + direccion[1]
        
            # Verificamos si la posición es válida sin lanzar excepción
            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
                if otra_pieza is None:  
                    posiciones.append((nueva_fila, nueva_columna))
                elif otra_pieza.__color__ != self.__color__:  
                    posiciones.append((nueva_fila, nueva_columna))
        
        return posiciones
