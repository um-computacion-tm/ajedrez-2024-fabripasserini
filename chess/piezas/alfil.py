from chess.piezas.pieza import Pieza

class Alfil(Pieza):
    blanco_str = "♝"
    negro_str = "♗"
    
    def posiciones_validas(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        posible_posiciones = (
        self.posibles_posiciones_diagonal_dd(desde_fila, desde_columna) +
            self.posibles_posiciones_diagonal_id(desde_fila, desde_columna) +
            self.posibles_posiciones_diagonal_ia(desde_fila, desde_columna) +
            self.posibles_posiciones_diagonal_da(desde_fila, desde_columna)
        )
        return (hasta_fila, hasta_columna) in posible_posiciones

    def posibles_posiciones_diagonal_dd(self, fila, columna):
        posibles = []
        siguiente_fila, siguiente_columna = fila + 1, columna + 1
        while siguiente_fila < 8 and siguiente_columna < 8:
            otra_pieza = self.__tablero__.obtener_pieza(siguiente_fila, siguiente_columna)
            if otra_pieza is not None:
                if otra_pieza.__color__ != self.__color__:
                    posibles.append((siguiente_fila, siguiente_columna))
                break
            posibles.append((siguiente_fila, siguiente_columna))
            siguiente_fila += 1
            siguiente_columna += 1
        return posibles

    def posibles_posiciones_diagonal_id(self, fila, columna):
        posibles = []
        siguiente_fila, siguiente_columna = fila + 1, columna - 1
        while siguiente_fila < 8 and siguiente_columna >= 0:
            otra_pieza = self.__tablero__.obtener_pieza(siguiente_fila, siguiente_columna)
            if otra_pieza is not None:
                if otra_pieza.__color__ != self.__color__:
                    posibles.append((siguiente_fila, siguiente_columna))
                break
            posibles.append((siguiente_fila, siguiente_columna))
            siguiente_fila += 1
            siguiente_columna -= 1
        return posibles

    def posibles_posiciones_diagonal_da(self, fila, columna):
        posibles = []
        siguiente_fila, siguiente_columna = fila - 1, columna + 1
        while siguiente_fila >= 0 and siguiente_columna < 8:
            otra_pieza = self.__tablero__.obtener_pieza(siguiente_fila, siguiente_columna)
            if otra_pieza is not None:
                if otra_pieza.__color__ != self.__color__:
                    posibles.append((siguiente_fila, siguiente_columna))
                break
            posibles.append((siguiente_fila, siguiente_columna))
            siguiente_fila -= 1
            siguiente_columna += 1
        return posibles

    def posibles_posiciones_diagonal_ia(self, fila, columna):
        posibles = []
        siguiente_fila, siguiente_columna = fila - 1, columna - 1
        while siguiente_fila >= 0 and siguiente_columna >= 0:
            otra_pieza = self.__tablero__.obtener_pieza(siguiente_fila, siguiente_columna)
            if otra_pieza is not None:
                if otra_pieza.__color__ != self.__color__:
                    posibles.append((siguiente_fila, siguiente_columna))
                break
            posibles.append((siguiente_fila, siguiente_columna))
            siguiente_fila -= 1
            siguiente_columna -= 1
        return posibles