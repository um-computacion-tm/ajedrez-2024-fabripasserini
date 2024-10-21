from chess.piezas.alfil import Alfil
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.torre import Torre
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon
from chess.excepciones import *

class Tablero:
    """
    Clase que representa un tablero de ajedrez. Inicializa las piezas en sus posiciones
    estándar o vacía el tablero si se utiliza el modo `for_test`.
    
    Atributos:
        __posiciones__: lista bidimensional que almacena las piezas en el tablero.
    """
    def __init__(self, for_test=False):
        """
        Inicializa un tablero de ajedrez con las piezas en sus posiciones iniciales o vacío
        si se pasa el parámetro `for_test` como True.

        Args:
            for_test (bool): Si es True, el tablero se inicializa vacío.
        """
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
        """
        Obtiene la pieza en una posición específica del tablero.

        Args:
            fila (int): La fila de la pieza.
            columna (int): La columna de la pieza.

        Returns:
            Pieza: La pieza en la posición solicitada, o None si no hay ninguna.

        Raises:
            fuera_del_tablero: Si las coordenadas están fuera del tablero.
        """
        if not (0 <= fila < 8 or 0 <= columna < 8):
            raise fuera_del_tablero()
        return self.__posiciones__[fila][columna]

    def poner_pieza(self, fila, columna, pieza):
        """
        Coloca una pieza en una posición específica del tablero.

        Args:
            fila (int): La fila donde colocar la pieza.
            columna (int): La columna donde colocar la pieza.
            pieza (Pieza): La pieza a colocar.
        """
        self.__posiciones__[fila][columna] = pieza

    def cambiar_posiciones(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        """
        Mueve una pieza de una posición a otra en el tablero.

        Args:
            desde_fila (int): Fila de la posición original.
            desde_columna (int): Columna de la posición original.
            hasta_fila (int): Fila de la nueva posición.
            hasta_columna (int): Columna de la nueva posición.
        """
        pieza = self.__posiciones__[desde_fila][desde_columna]
        self.__posiciones__[hasta_fila][hasta_columna] = pieza
        self.__posiciones__[desde_fila][desde_columna] = None

    def imprimir_tablero(self):
        """
        Imprime el tablero en consola, mostrando las piezas y posiciones vacías.
        """
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
        """
        Vacía el tablero, dejando todas las posiciones sin piezas.
        """
        self.__posiciones__ = [[None for _ in range(8)] for _ in range(8)]

    def obtener_rey_blanco(self):
        """
        Busca y retorna el rey blanco en el tablero.

        Returns:
            Rey: El rey blanco, o None si no se encuentra.
        """
        for fila in range(8):
            for columna in range(8):
                pieza = self.__posiciones__[fila][columna]
                if isinstance(pieza, Rey) and pieza.obtener_color() == "BLANCO":
                    return pieza
        return None

    def obtener_rey_negro(self):
        """
        Busca y retorna el rey negro en el tablero.

        Returns:
            Rey: El rey negro, o None si no se encuentra.
        """
        for fila in range(8):
            for columna in range(8):
                pieza = self.__posiciones__[fila][columna]
                if isinstance(pieza, Rey) and pieza.obtener_color() == "NEGRO":
                    return pieza
        return None
    
    def verificar_estado_juego(self):
        """
        Verifica el estado del juego, determinando si uno de los jugadores ha perdido
        todas sus piezas.

        Returns:
            str: "BLANCO" si las piezas blancas ganan, "NEGRO" si las negras ganan, 
            o "CONTINUA" si el juego sigue en curso.
        """
        piezas_blancas = 0
        piezas_negras = 0

        for fila in range(8):
            for columna in range(8):
                pieza = self.obtener_pieza(fila, columna)
                if pieza is not None:
                    if pieza.obtener_color() == "BLANCO":
                        piezas_blancas += 1
                    elif pieza.obtener_color() == "NEGRO":
                        piezas_negras += 1
        
        if piezas_blancas == 0:
            print("Las piezas negras ganan. No quedan piezas blancas. Fin del juego.")
            return "NEGRO"
        elif piezas_negras == 0:
            print("Las piezas blancas ganan. No quedan piezas negras. Fin del juego.")
            return "BLANCO"
        else:
            return "CONTINUA"

if __name__ == "__main__":  
    tablero = Tablero()





    