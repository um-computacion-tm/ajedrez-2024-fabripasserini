from chess.piezas.alfil import Alfil
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.torre import Torre
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon
from chess.excepciones import *


class Tablero:
    def __init__(self, for_test = False):
            self.__posiciones__ = []
            for _ in range(8):
                columna = []
                for _ in range(8):
                    columna.append(None)
                self.__posiciones__.append(columna)
            
            if not for_test:

                self.__posiciones__[0][0] = Torre("NEGRO", self) 
                self.__posiciones__[0][7] = Torre("NEGRO", self) 
                self.__posiciones__[7][7] = Torre("BLANCO", self) 
                self.__posiciones__[7][0] = Torre("BLANCO", self)


                for i in range(8):
                    self.__posiciones__[1][i] = Peon("NEGRO", self)
                    self.__posiciones__[6][i] = Peon("BLANCO", self)

        
                self.__posiciones__[0][1] = Caballo("NEGRO", self)
                self.__posiciones__[0][6] = Caballo("NEGRO", self)
                self.__posiciones__[7][1] = Caballo("BLANCO", self)  
                self.__posiciones__[7][6] = Caballo("BLANCO", self)

            
                self.__posiciones__[0][2] = Alfil("NEGRO", self)  
                self.__posiciones__[0][5] = Alfil("NEGRO", self)
                self.__posiciones__[7][2] = Alfil("BLANCO", self)
                self.__posiciones__[7][5] = Alfil("BLANCO", self)

            
                self.__posiciones__[0][3] = Dama("NEGRO", self)
                self.__posiciones__[7][3] = Dama("BLANCO", self)

                self.__posiciones__[0][4] = Rey("NEGRO", self)
                self.__posiciones__[7][4] = Rey("BLANCO", self)
        
        
    def obtener_pieza(self, fila, columna):
            if not (0 <= fila < 8 or 0 <= columna < 8):
                raise fuera_del_tablero()
            return self.__posiciones__[fila][columna]

    def poner_pieza(self, fila, columna, pieza):
            self.__posiciones__[fila][columna] = pieza

    def cambiar_posiciones(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        pieza = self.__posiciones__[desde_fila][desde_columna]  # Obtener la pieza de la posición de origen
        self.__posiciones__[hasta_fila][hasta_columna] = pieza  # Mover la pieza a la nueva posición
        self.__posiciones__[desde_fila][desde_columna] = None 

    def imprimir_tablero(self):
        print("   0|1|2|3|4|5|6|7")
        for i, fila in enumerate(self.__posiciones__):
            cadena = f"{i}- "
            for pieza in fila:
                if pieza is None:
                    cadena += ". "
                else:
                    cadena += str(pieza) + " "
            print(cadena)

    def vaciar_tablero(self):
        self.__posiciones__ = [[None for _ in range(8)] for _ in range(8)]

    def obtener_rey_blanco(self):
        for fila in range(8):
            for columna in range(8):
                pieza = self.__posiciones__[fila][columna]  
                if isinstance(pieza, Rey) and pieza.obtener_color() == "BLANCO":
                    return pieza
        return None 

    def obtener_rey_negro(self):
        for fila in range(8):
            for columna in range(8):
                pieza = self.__posiciones__[fila][columna]  
                if isinstance(pieza, Rey) and pieza.obtener_color() == "NEGRO":
                    return pieza
        return None  

if __name__ == "__main__":  
    tablero = Tablero()




    