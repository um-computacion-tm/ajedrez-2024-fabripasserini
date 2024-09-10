from chess.piezas.alfil import Alfil
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.torre import Torre
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon



class Tablero:
    def __init__(self):
        self.__posiciones = []
        for _ in range(8):
            columna = []
            for _ in range(8):
                columna.append(None)
            self.__posiciones.append(columna)
    
        self.__posiciones[0][0] = Torre("NEGRO", self) 
        self.__posiciones[0][7] = Torre("NEGRO", self) 
        self.__posiciones[7][7] = Torre("BLANCO", self) 
        self.__posiciones[7][0] = Torre("BLANCO", self)


        for i in range(8):
            self.__posiciones[1][i] = Peon("NEGRO", self)
            self.__posiciones[6][i] = Peon("BLANCO", self)

    
        self.__posiciones[0][1] = Caballo("NEGRO", self)
        self.__posiciones[0][6] = Caballo("NEGRO", self)
        self.__posiciones[7][1] = Caballo("BLANCO", self)  
        self.__posiciones[7][6] = Caballo("BLANCO", self)

        
        self.__posiciones[0][2] = Alfil("NEGRO", self)  
        self.__posiciones[0][5] = Alfil("NEGRO", self)
        self.__posiciones[7][2] = Alfil("BLANCO", self)
        self.__posiciones[7][5] = Alfil("BLANCO", self)

        
        self.__posiciones[0][3] = Dama("NEGRO", self)
        self.__posiciones[7][3] = Dama("BLANCO", self)

        self.__posiciones[0][4] = Rey("NEGRO", self)
        self.__posiciones[7][4] = Rey("BLANCO", self)
    
    def __str__(self):
        tablero_str = ""
        for fila in self.__posiciones:
            for cell in fila:
                if cell is not None:
                    tablero_str += str(cell)
                else:
                    tablero_str += " "
            tablero_str += "\n"
        return tablero_str
    
    
    def mostrar_tablero(self):
        for fila in self.__posiciones:
            fila_str = ""
            for pieza in fila:
                if pieza is None:
                    fila_str += ". "
                else:
                    fila_str += str(pieza) + " "
            print(fila_str)

if __name__ == "__main__":
    tablero = Tablero()
    tablero.mostrar_tablero()
    

    
    
 


    