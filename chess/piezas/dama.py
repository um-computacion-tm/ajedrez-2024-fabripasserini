from chess.piezas.pieza import Pieza  # Importamos la clase Pieza
from chess.excepciones import *  # Importamos las excepciones


class Dama(Pieza):
    """
    Clase que representa una dama en el juego de ajedrez.

    Atributos:
        blanco_str (str): Representación de la dama blanca.
        negro_str (str): Representación de la dama negra.
    """

    blanco_str = "♛"
    negro_str = "♕"

    def __init__(self, color, tablero):
        """
        Inicializa una dama con su color y el tablero asociado.

        Args:
            color (str): Color de la dama, "BLANCO" o "NEGRO".
            tablero (Tablero): Instancia del tablero donde se posiciona la dama.
        """
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Combina los movimientos en todas las direcciones posibles (diagonales, verticales, horizontales).

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones válidas a las que la dama puede moverse.
        """
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))
        return posibles

    def es_casilla_vacia(self, fila, columna):
        """
        Verifica si una casilla está vacía en el tablero.

        Args:
            fila (int): Fila de la casilla.
            columna (int): Columna de la casilla.

        Returns:
            bool: True si la casilla está vacía, False si no lo está.
        """
        return self.__tablero__.obtener_pieza(fila, columna) is None

    def es_posicion_valida(self, fila, columna):
        """
        Verifica si la posición está dentro de los límites del tablero.

        Args:
            fila (int): Fila de la posición a verificar.
            columna (int): Columna de la posición a verificar.

        Returns:
            bool: True si la posición es válida.

        Raises:
            fuera_del_tablero: Si la posición está fuera de los límites del tablero.
        """
        if not (0 <= fila < 8 and 0 <= columna < 8):
            raise fuera_del_tablero(f"La posición ({fila}, {columna}) está fuera de los límites del tablero.")
        return True

    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        """
        Devuelve todas las posiciones válidas a las que la dama puede moverse.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones válidas a las que la dama puede moverse.
        """
        posiciones = []
        posiciones.extend(self.obtener_posiciones_diagonales(desde_fila, desde_columna))
        posiciones.extend(self.obtener_posiciones_verticales(desde_fila, desde_columna))
        posiciones.extend(self.obtener_posiciones_horizontales(desde_fila, desde_columna))
        return posiciones
    
    def obtener_posiciones_diagonales(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones diagonales a las que la dama puede moverse.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones diagonales válidas.
        """
        posiciones = []
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Las 4 direcciones diagonales
    
        for direccion in direcciones:
            nueva_fila = desde_fila
            nueva_columna = desde_columna
            
            while True:
                nueva_fila += direccion[0]
                nueva_columna += direccion[1]
                
                if not self.es_posicion_valida(nueva_fila, nueva_columna):
                    break
                
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)
                if otra_pieza is None: 
                    posiciones.append((nueva_fila, nueva_columna))  # Casilla vacía, sigue avanzando
                elif otra_pieza.obtener_color() != self.__color__:  
                    posiciones.append((nueva_fila, nueva_columna))  # Captura y se detiene
                    break
                else:
                    break  # Si hay una pieza aliada, se detiene
    
        return posiciones

    def obtener_posiciones_verticales(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones verticales a las que la dama puede moverse.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones verticales válidas.
        """
        posiciones = []
        # Movimiento vertical hacia arriba y hacia abajo
        for desplazamiento in [-1, 1]:  
            nueva_fila = desde_fila
            while True:
                nueva_fila += desplazamiento
                if not self.es_posicion_valida(nueva_fila, desde_columna):
                    break
                
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, desde_columna)
                if otra_pieza is None:
                    posiciones.append((nueva_fila, desde_columna))  # Casilla vacía
                elif otra_pieza.obtener_color() != self.__color__:
                    posiciones.append((nueva_fila, desde_columna))  # Captura y se detiene
                    break
                else:
                    break  # Bloqueado por pieza aliada

        return posiciones

    def obtener_posiciones_horizontales(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones horizontales a las que la dama puede moverse.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones horizontales válidas.
        """
        posiciones = []
    
        # Recorremos todas las columnas hacia la derecha
        for nueva_columna in range(desde_columna + 1, 8):
            if not self.es_posicion_valida(desde_fila, nueva_columna):
                break  # Si no es válida (fuera del tablero), se detiene
            otra_pieza = self.__tablero__.obtener_pieza(desde_fila, nueva_columna)
            if otra_pieza is None:
                posiciones.append((desde_fila, nueva_columna))  # Casilla vacía
            elif otra_pieza.obtener_color() != self.__color__:
                posiciones.append((desde_fila, nueva_columna))  # Captura
                break  # Detiene después de capturar
            else:
                break  # Detiene si encuentra una pieza aliada

        # Recorremos todas las columnas hacia la izquierda
        for nueva_columna in range(desde_columna - 1, -1, -1):
            if not self.es_posicion_valida(desde_fila, nueva_columna):
                break  # Si no es válida, se detiene
            otra_pieza = self.__tablero__.obtener_pieza(desde_fila, nueva_columna)
            if otra_pieza is None:
                posiciones.append((desde_fila, nueva_columna))  # Casilla vacía
            elif otra_pieza.obtener_color() != self.__color__:
                posiciones.append((desde_fila, nueva_columna))  # Captura
                break  # Detiene después de capturar
            else:
                break  # Detiene si encuentra una pieza aliada

        return posiciones
