from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Torre(Pieza):
    blanco_str = "♜"
    negro_str = "♖"
    
    def obtener_posibles_posiciones(self, desde_fila, desde_columna): # Devuelve todas las posiciones posibles a las que la torre puede moverse
        posibles = []
        posibles.extend(self.obtener_posiciones_verticales(desde_fila, desde_columna))
        posibles.extend(self.obtener_posiciones_horizontales(desde_fila, desde_columna))
        return posibles

    def es_casilla_vacia(self, fila, columna):  # Verifica si una casilla está vacía en el tablero.
        return self.__tablero__.obtener_pieza(fila, columna) is None

    def es_posicion_valida(self, fila, columna):  # Verifica si la posición está dentro de los límites del tablero.
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True
    
    def obtener_posiciones_verticales(self, desde_fila, desde_columna):  # Obtiene todas las posiciones válidas a lo largo de la columna.
        posiciones = []

        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, 1, 0))
        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, -1, 0))

        return posiciones

    def obtener_posiciones_horizontales(self, desde_fila, desde_columna): # Obtiene todas las posiciones válidas a lo largo de la fila.
        posiciones = []

        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, 0, 1))
        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, 0, -1))

        return posiciones

    def obtener_posiciones_en_direccion(self, desde_fila, desde_columna, incremento_fila, incremento_columna): # Obtiene posiciones válidas en una dirección (vertical u horizontal).
        posiciones = []
        fila_actual = desde_fila + incremento_fila
        columna_actual = desde_columna + incremento_columna

        while self.es_posicion_valida(fila_actual, columna_actual):
            if self.es_casilla_vacia(fila_actual, columna_actual):
                posiciones.append((fila_actual, columna_actual))
            else:
                otra_pieza = self.__tablero__.obtener_pieza(fila_actual, columna_actual)
                if otra_pieza.__color__ != self.__color__:
                    posiciones.append((fila_actual, columna_actual))  
                else:
                    raise movimiento_inválido(f"No puedes capturar tu propia pieza en ({fila_actual}, {columna_actual}).")
                break  

            fila_actual += incremento_fila
            columna_actual += incremento_columna

        return posiciones