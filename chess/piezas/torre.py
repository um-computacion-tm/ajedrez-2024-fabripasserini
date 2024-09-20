from chess.piezas.pieza import Pieza

class Torre(Pieza):
    blanco_str = "♜"
    negro_str = "♖"
    
    def posiciones_validas(
        self,
        desde_fila,
        desde_columna,
        hasta_fila,
        hasta_columna,
    ):
        posible_posiciones = (
            self.posibles_posiciones_vd(desde_fila, desde_columna) +
            self.posibles_posiciones_va(desde_fila, desde_columna)
        )
        return (hasta_fila, hasta_columna) in posible_posiciones

    def posibles_posiciones_vd(self, fila, columna):
        posibles = []
        for siguente_fila in range(fila + 1, 8):
            otra_pieza = self.__tablero__.obtener_pieza(siguente_fila, columna)
            if otra_pieza is not None:
                if otra_pieza.__color__ != self.__color__:
                    posibles.append((siguente_fila, columna))
                break
            posibles.append((siguente_fila, columna))
        return posibles

    def posibles_posiciones_va(self, fila, columna):
        posibles = []
        for siguente_fila in range(fila - 1, -1, -1):
            posibles.append((siguente_fila, columna))
        return posibles
