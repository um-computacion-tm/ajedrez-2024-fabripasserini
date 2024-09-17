from chess.piezas.pieza import Pieza


class Peon(Pieza):
    blanco_str = "♟"
    negro_str = "♙"

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
       pass

    def obtener_posibles_comer(self, desde_fila, dese_columna):
        if self.__color__ == "NEGRO":
            otra_pieza = self.__tablero__.obtener_pieza(desde_fila + 1, dese_columna + 1)
            if otra_pieza and otra_pieza.__color__ == "BLANCO":
                return [(desde_fila + 1, dese_columna + 1)]

        return []