from chess.tablero import Tablero

class Ajedrez:
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCO"

    def mover(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        if not self.__es_posicion_valida(desde_fila, desde_columna) or not self.__es_posicion_valida(hasta_fila, hasta_columna):
            raise ValueError("Posiciones no válidas")

        pieza = self.__obtener_pieza(desde_fila, desde_columna)
        if pieza == ' ':
            raise ValueError("No hay pieza en la posición de origen")
        
        self.__tablero__.__casillas__[hasta_fila][hasta_columna] = pieza
        self.__tablero__.__casillas__[desde_fila][desde_columna] = ' '

        self.cambiar_turno()

    def __es_posicion_valida(self, fila, columna):
        return 0 <= fila < 8 and 0 <= columna < 8

    def __obtener_pieza(self, fila, columna):
        return self.__tablero__.__casillas__[fila][columna]

    @property
    def turno(self):
        return self.__turno__

    def mostrar_tablero(self):
        self.__tablero__.mostrar_tablero()

    def cambiar_turno(self):
        if self.__turno__ == "BLANCO":
            self.__turno__ = "NEGRO"
        else:
            self.__turno__ = "BLANCO"
