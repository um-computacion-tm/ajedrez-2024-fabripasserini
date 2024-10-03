from chess.piezas.alfil import Alfil
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.torre import Torre
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon
from chess.excepciones import fuera_del_tablero


class Tablero:
    def __init__(self, for_test = False):
            self.__posiciones__ = []
            for _ in range(8):
                columna = []
                for _ in range(8):
                    columna.append(None)
                self.__posiciones__.append(columna)
            if for_test:
                 self.insertar_piezas()
    def insertar_piezas(self):
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
        
    
        
    def obtener_tablero(self):
            
            tablero = []
            for fila in self.__posiciones__:
                fila_actual = []
                for pieza in fila:
                    if pieza is not None:
                        fila_actual.append(str(pieza))  
                    else:
                        fila_actual.append(" ") 
                tablero.append(fila_actual)
            return tablero
        
    def obtener_pieza(self, fila, columna):
            if not (0 <= fila < 8 or 0 <= columna < 8):
                raise fuera_del_tablero()
            return self.__posiciones__[fila][columna]

    def poner_pieza(self, fila, columna, pieza):
            self.__posiciones__[fila][columna] = pieza

    def mover(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
            origen = self.obtener_pieza(desde_fila, desde_columna)
            self.poner_pieza(hasta_fila, hasta_columna, origen)
            self.poner_pieza(desde_fila, desde_columna, None)

    def obtener_color_pieza(self, fila, columna):
            pieza = self.obtener_pieza(fila, columna)
            if pieza is not None:
                return pieza.obtener_color()
            return None
        
    def movimiento_valido(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
            
            pieza = self.obtener_pieza(desde_fila, desde_columna)
            if pieza is None:
                return False
            possible_moves = pieza.posiciones_validas(desde_fila, desde_columna, hasta_fila, hasta_columna)
            return (hasta_fila, hasta_columna) in possible_moves
            
if __name__ == "__main__":  
    tablero = Tablero()