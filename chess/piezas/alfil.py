from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Alfil(Pieza):
    blanco_str = "♝"
    negro_str = "♗"
    
    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna): # Devuelve todas las posiciones posibles a las que el alfil puede moverse
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles

    def es_casilla_vacia(self, fila, columna): # Verifica si una casilla está vacía en el tablero.
        return self.__tablero__.obtener_pieza(fila, columna) is None
    
    def es_posicion_valida(self, fila, columna): # Verifica si la posición está dentro de los límites del tablero.
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True

    def obtener_posiciones_mover(self, fila, columna):
        posiciones = []
    
    # Diagonales: (arriba-izquierda, arriba-derecha, abajo-izquierda, abajo-derecha)
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
        for direccion in direcciones:
            nueva_fila, nueva_columna = fila + direccion[0], columna + direccion[1]
        
            while self.es_posicion_valida(nueva_fila, nueva_columna):
                pieza_en_casilla = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
            
                if pieza_en_casilla is None:
                    posiciones.append((nueva_fila, nueva_columna))
                else:
                    if pieza_en_casilla.obtener_color() != self.obtener_color():
                    # Puede capturar la pieza enemiga
                        posiciones.append((nueva_fila, nueva_columna))
                # No puede saltar sobre ninguna pieza, sea amiga o enemiga
                break
            
            # Avanzar en la dirección actual
            nueva_fila += direccion[0]
            nueva_columna += direccion[1]

        return posiciones
