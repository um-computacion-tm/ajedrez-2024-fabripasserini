from chess.tablero import Tablero
from chess.excepciones import *
from chess.piezas.rey import Rey

class Ajedrez:
    
    def __init__(self):
        self.__tablero__ = Tablero()
        self.__turno__ = "BLANCO"
        self.__terminar_partida__ = False
        self.__ganador__ = None
        self.__rey_blanco__ = self.__tablero__.obtener_rey_blanco()  # Asumiendo que hay un método que obtiene los reyes
        self.__rey_negro__ = self.__tablero__.obtener_rey_negro()

    def en_juego(self):
        return True
    
    def en_tablero(self, fila, columna):
        return 0 <= fila < 8 and 0 <= columna < 8

    def mover_pieza(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        origen = self.__tablero__.obtener_pieza(desde_fila, desde_columna)
        destino = self.__tablero__.obtener_pieza(hasta_fila, hasta_columna)
        if not (self.en_tablero(desde_fila, desde_columna) and self.en_tablero(hasta_fila, hasta_columna)):
            raise fuera_del_tablero
       
        elif origen is None:
            raise movimiento_sin_pieza

        elif origen.obtener_color() != self.__turno__:
            raise turno_invalido
        
        
        elif desde_fila == hasta_fila and desde_columna == hasta_columna:
            raise movimiento_inválido

        
        elif destino is not None and destino.obtener_color() == self.__turno__:
            raise movimiento_inválido
        
        if (hasta_fila, hasta_columna) not in origen.obtener_posibles_posiciones(desde_fila, desde_columna):
            raise movimiento_inválido

        
        self.__tablero__.poner_pieza(hasta_fila, hasta_columna, origen)
        self.__tablero__.poner_pieza(desde_fila, desde_columna, None)
        

        if isinstance(destino, Rey):
            self.__terminar_partida__ = True
            self.__ganador__ = self.__turno__
            self.terminar_partida()
        else:
            self.cambiar_turno()
        
    def turnos(self):
        return self.__turno__

    def mostrar_tablero(self):
        print()
        print("Tablero de juego")
        self.__tablero__.imprimir_tablero()

    def cambiar_turno(self):
        if self.__turno__ == "BLANCO":
            self.__turno__ = "NEGRO"
        else:
            self.__turno__ = "BLANCO"
    
    def ganador(self):
        if self.__terminar_partida__:
            if self.__turno__ == "BLANCO":
                return "NEGRO"
            else:
                return "BLANCO"
        return None
    
    def terminar_partida(self):
        self.__terminar_partida__ = True
        print("Gana el jugador", self.ganador())
        

    

       