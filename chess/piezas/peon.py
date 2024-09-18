from chess.piezas.pieza import Pieza


class Peon(Pieza):
    blanco_str = "♟"
    negro_str = "♙"

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        posibles = self.obtener_posiciones_mover(desde_fila, desde_columna)
        posibles.extend(
            self.obtener_posibles_comer(desde_fila, desde_columna)
        )
        return posibles

    def obtener_posibles_comer(self, desde_fila, dese_columna):
        if self.__color__ == "NEGRO":
            otra_pieza = self.__tablero__.obtener_pieza(desde_fila + 1, dese_columna + 1)
            if otra_pieza and otra_pieza.__color__ == "BLANCO":
                return [(desde_fila + 1, dese_columna + 1)]

        return []
    
    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        if self.__color__ == "NEGRO":
            if self.__tablero__.obtener_pieza(desde_fila + 1, desde_columna) is None:
                if (
                    desde_fila == 1 and
                    self.__tablero__.obtener_pieza(desde_fila + 2, desde_columna) is None
                ):
                    return [
                        (desde_fila + 1, desde_columna),
                        (desde_fila + 2, desde_columna)
                    ]
                else:
                    return [
                        (desde_fila + 1, desde_columna),
                    ]
        else:
            if desde_fila == 6:
                return [
                    (desde_fila - 1, desde_columna),
                    (desde_fila - 2, desde_columna)
                ]
            else:
                if self.__tablero__.obtener_pieza(desde_fila - 1, desde_columna) is None:
                    return [
                        (desde_fila - 1, desde_columna),
                    ]
                else:
                    return []
        return []