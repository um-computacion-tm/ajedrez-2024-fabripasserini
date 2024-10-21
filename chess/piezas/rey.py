from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Rey(Pieza):
    """
    Clase que representa la pieza del Rey en el ajedrez, hereda de Pieza.

    Atributos:
        blanco_str (str): Representación del rey blanco.
        negro_str (str): Representación del rey negro.
    """

    blanco_str = "♚"
    negro_str = "♔"

    def __init__(self, color, tablero):
        """
        Inicializa un rey con un color y un tablero asociado.

        Args:
            color (str): Color de la pieza, "BLANCO" o "NEGRO".
            tablero (Tablero): Instancia del tablero donde se posiciona la pieza.
        """
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Devuelve todas las posiciones posibles a las que el rey puede moverse desde su posición actual.

        Args:
            desde_fila (int): Fila actual del rey.
            desde_columna (int): Columna actual del rey.

        Returns:
            list: Lista de tuplas con las coordenadas (fila, columna) a las que el rey puede moverse.
        """
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles

    def es_casilla_vacia(self, fila, columna):
        """
        Verifica si una casilla en el tablero está vacía.

        Args:
            fila (int): La fila de la casilla a verificar.
            columna (int): La columna de la casilla a verificar.

        Returns:
            bool: True si la casilla está vacía, False si contiene una pieza.
        """
        return self.__tablero__.obtener_pieza(fila, columna) is None
    
    def es_posicion_valida(self, fila, columna):
        """
        Verifica si una posición está dentro de los límites del tablero.

        Args:
            fila (int): La fila a verificar.
            columna (int): La columna a verificar.

        Raises:
            fuera_del_tablero: Si la posición está fuera de los límites del tablero.

        Returns:
            bool: True si la posición es válida, False si no.
        """
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True

    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        """
        Obtiene las posiciones a las que el rey puede moverse, teniendo en cuenta las reglas del juego.
        El rey puede moverse una casilla en cualquier dirección (horizontal, vertical o diagonal).

        Args:
            desde_fila (int): Fila de origen del rey.
            desde_columna (int): Columna de origen del rey.

        Returns:
            list: Lista de tuplas con las coordenadas (fila, columna) de las posiciones posibles.
        """
        posiciones = []
        direcciones = [
            (-1, 0), (1, 0), (0, -1), (0, 1), 
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
    
        for direccion in direcciones:
            nueva_fila = desde_fila + direccion[0]
            nueva_columna = desde_columna + direccion[1]
        
            # Verificamos si la posición es válida sin lanzar excepción
            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
                if otra_pieza is None:  # La casilla está vacía
                    posiciones.append((nueva_fila, nueva_columna))
                elif otra_pieza.__color__ != self.__color__:  # Hay una pieza del oponente
                    posiciones.append((nueva_fila, nueva_columna))
        
        return posiciones

