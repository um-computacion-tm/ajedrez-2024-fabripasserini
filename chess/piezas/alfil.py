from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Alfil(Pieza):
    blanco_str = "♝"
    negro_str = "♗"

    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Devuelve todas las posiciones posibles a las que el alfil puede moverse.
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
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True

    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones válidas donde el alfil puede moverse en diagonal.
        """
        posiciones = []
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Direcciones diagonales

        for direccion in direcciones:
            nueva_fila, nueva_columna = desde_fila, desde_columna

            while True:
                nueva_fila += direccion[0]
                nueva_columna += direccion[1]

                try:
                    self.es_posicion_valida(nueva_fila, nueva_columna)
                except fuera_del_tablero:
                    break  # Salir si la posición no es válida

                pieza_en_casilla = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)

                if pieza_en_casilla is None:
                    posiciones.append((nueva_fila, nueva_columna))  # Casilla vacía, puede moverse
                else:
                    if pieza_en_casilla.obtener_color() != self.obtener_color():
                        posiciones.append((nueva_fila, nueva_columna))  # Puede capturar la pieza enemiga
                    break  # Se encuentra con una pieza, no puede saltar más allá

        return posiciones
