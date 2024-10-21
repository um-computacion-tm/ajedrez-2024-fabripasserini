from chess.piezas.pieza import Pieza
from chess.excepciones import *

class Peon(Pieza):
    """
    Clase que representa un peón en el juego de ajedrez.

    Atributos:
        blanco_str (str): Representación del peón blanco.
        negro_str (str): Representación del peón negro.
    """

    blanco_str = "♟"
    negro_str = "♙"

    def __init__(self, color, tablero):
        """
        Inicializa un peón con su color y el tablero asociado.

        Args:
            color (str): Color del peón, "BLANCO" o "NEGRO".
            tablero (Tablero): Instancia del tablero donde se posiciona el peón.
        """
        super().__init__(color, tablero)

    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        """
        Devuelve todas las posiciones posibles a las que el peón puede moverse,
        tanto hacia adelante como capturando en diagonal.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones válidas a las que el peón puede moverse.
        """
        posibles = []
        posibles.extend(self.obtener_posiciones_mover(desde_fila, desde_columna))  # Movimiento hacia adelante
        posibles.extend(self.obtener_posibles_comer(desde_fila, desde_columna))    # Captura diagonal
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

    def obtener_posibles_comer(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones diagonales donde el peón puede capturar una pieza enemiga.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones donde el peón puede capturar.
        """
        posiciones_comer = []
       
        if self.__color__ == "NEGRO":
            direcciones = [(1, 1), (1, -1)]  # Diagonales hacia adelante para peón negro
        else:
            direcciones = [(-1, 1), (-1, -1)]  # Diagonales hacia adelante para peón blanco

        for direccion in direcciones:
            nueva_fila = desde_fila + direccion[0]
            nueva_columna = desde_columna + direccion[1]

            if 0 <= nueva_fila < 8 and 0 <= nueva_columna < 8:
                otra_pieza = self.__tablero__.obtener_pieza(nueva_fila, nueva_columna)

                # Verificamos que haya una pieza enemiga en la casilla diagonal
                if otra_pieza and otra_pieza.obtener_color() != self.__color__:
                    posiciones_comer.append((nueva_fila, nueva_columna))

        return posiciones_comer

    def obtener_posiciones_mover(self, desde_fila, desde_columna):
        """
        Devuelve las posiciones válidas a las que el peón puede moverse hacia adelante.

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.

        Returns:
            list: Lista de tuplas que representan posiciones donde el peón puede avanzar.
        """
        posiciones = []
        if self.__color__ == "NEGRO":
            avance = 1
            fila_inicial = 1
        else:
            avance = -1
            fila_inicial = 6

        # Movimiento simple hacia adelante
        posiciones.extend(self.obtener_posicion_simple(desde_fila, desde_columna, avance))
        # Movimiento inicial doble (si es el primer movimiento)
        posiciones.extend(self.obtener_posicion_inicial_doble(desde_fila, desde_columna, avance, fila_inicial))

        return posiciones

    def obtener_posicion_simple(self, desde_fila, desde_columna, avance):
        """
        Obtiene la posición de movimiento simple (una casilla hacia adelante).

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.
            avance (int): La dirección del movimiento (1 o -1).

        Returns:
            list: Lista de tuplas que representan la posición simple hacia adelante.

        Raises:
            movimiento_inválido: Si hay una pieza bloqueando el movimiento.
        """
        nueva_fila = desde_fila + avance
        posiciones = []

        if self.es_posicion_valida(nueva_fila, desde_columna):  # Verifica si la posición es válida
            if self.es_casilla_vacia(nueva_fila, desde_columna):  # Verifica si la casilla está vacía
                posiciones.append((nueva_fila, desde_columna))  # Agregar la posición si está vacía
            else:
                # Solo lanzar la excepción si hay una pieza en la misma columna y no se intenta capturar
                raise movimiento_inválido(f"Hay una pieza bloqueando el movimiento en ({nueva_fila}, {desde_columna}).")

        return posiciones

    def obtener_posicion_inicial_doble(self, desde_fila, desde_columna, avance, fila_inicial):
        """
        Obtiene la posición inicial de dos casillas hacia adelante (si es el primer movimiento del peón).

        Args:
            desde_fila (int): Fila de la posición de origen.
            desde_columna (int): Columna de la posición de origen.
            avance (int): La dirección del movimiento (1 o -1).
            fila_inicial (int): Fila desde donde el peón puede avanzar dos casillas.

        Returns:
            list: Lista de tuplas que representan la posición inicial doble.

        Raises:
            movimiento_inválido: Si hay una pieza bloqueando el movimiento.
        """
        posiciones = []
        if desde_fila == fila_inicial:
            nueva_fila_dos = desde_fila + (2 * avance)
            if self.es_posicion_valida(nueva_fila_dos, desde_columna):
                # Verificamos que las dos casillas adelante estén vacías
                if self.es_casilla_vacia(nueva_fila_dos, desde_columna) and self.es_casilla_vacia(desde_fila + avance, desde_columna):
                    posiciones.append((nueva_fila_dos, desde_columna))
                else:
                    raise movimiento_inválido(f"Hay una pieza bloqueando el movimiento en ({nueva_fila_dos}, {desde_columna}).")

        return posiciones
