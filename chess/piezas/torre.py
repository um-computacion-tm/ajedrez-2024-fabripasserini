from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Torre(Pieza):
    blanco_str = "♜"
    negro_str = "♖"

    def __init__(self, color, tablero):
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Devuelve todas las posiciones posibles a las que la torre puede moverse,
        tanto en dirección vertical como horizontal.
        """
        posibles = []
        posibles.extend(self.obtener_posiciones_verticales(desde_fila, desde_columna))  # Movimiento vertical
        posibles.extend(self.obtener_posiciones_horizontales(desde_fila, desde_columna))  # Movimiento horizontal
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

    
    def obtener_posiciones_verticales(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones válidas en dirección vertical (hacia arriba y hacia abajo).
        """
        posiciones = []
        # Movimiento hacia arriba
        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, -1, 0))
        # Movimiento hacia abajo
        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, 1, 0))
        return posiciones

    def obtener_posiciones_horizontales(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones válidas en dirección horizontal (hacia izquierda y derecha).
        """
        posiciones = []
        # Movimiento hacia la izquierda
        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, 0, -1))
        # Movimiento hacia la derecha
        posiciones.extend(self.obtener_posiciones_en_direccion(desde_fila, desde_columna, 0, 1))
        return posiciones

    def obtener_posiciones_en_direccion(self, fila, columna, incremento_fila, incremento_columna):
        """
        Obtiene las posiciones en una dirección específica (vertical u horizontal).
        """
        posiciones = []
        fila_actual = fila + incremento_fila
        columna_actual = columna + incremento_columna

        # Sigue avanzando en la dirección especificada hasta que se salga del tablero o encuentre una pieza.
        while 0 <= fila_actual < 8 and 0 <= columna_actual < 8:
            if self.es_casilla_vacia(fila_actual, columna_actual):
                # Si la casilla está vacía, añade la posición como válida.
                posiciones.append((fila_actual, columna_actual))
                
            else:
                # Si hay una pieza, puede capturarla si es del color contrario.
                pieza_en_casilla = self.__tablero__.obtener_pieza(fila_actual, columna_actual)
                if pieza_en_casilla.obtener_color() != self.obtener_color():
                    posiciones.append((fila_actual, columna_actual))
                break  # Detener el bucle si hay una pieza (no puede saltar sobre otras).

            # Avanza a la siguiente casilla
            fila_actual += incremento_fila
            columna_actual += incremento_columna

        return posiciones




