from chess.excepciones import *

class Pieza():
    """
    Clase base que representa una pieza de ajedrez.

    Atributos:
        __color__ (str): Color de la pieza ("BLANCO" o "NEGRO").
        __tablero__ (Tablero): Instancia del tablero donde se encuentra la pieza.
    """

    def __init__(self, color, tablero):
        """
        Inicializa una pieza con su color y el tablero asociado.

        Args:
            color (str): Color de la pieza, "BLANCO" o "NEGRO".
            tablero (Tablero): Instancia del tablero donde se posiciona la pieza.
        """
        self.__color__ = color
        self.__tablero__ = tablero
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la pieza según su color.

        Returns:
            str: Símbolo que representa la pieza.
        """
        if self.__color__ == "BLANCO":
            return self.blanco_str
        else:
            return self.negro_str
        
    def obtener_color(self):
        """
        Obtiene el color de la pieza.

        Returns:
            str: Color de la pieza.
        """
        return self.__color__
    
    def posiciones_validas(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        """
        Verifica si el movimiento a una posición específica es válido.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.
            hasta_fila (int): Fila de la posición de destino.
            hasta_columna (int): Columna de la posición de destino.

        Returns:
            bool: True si el movimiento es válido, False si no lo es.
        """
        posibles_posiciones = self.obtener_posibles_posiciones(desde_fila, desde_columna)
        return (hasta_fila, hasta_columna) in posibles_posiciones
    
    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Método abstracto que debe ser implementado en las subclases.
        Debe devolver las posiciones posibles a las que la pieza puede moverse.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Raises:
            NotImplementedError: Si no es implementado en la subclase.
        """
        raise NotImplementedError("Este método debe ser implementado en las subclases.")


    
    
    
    
    
  
  