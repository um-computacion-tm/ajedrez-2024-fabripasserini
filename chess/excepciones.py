class movimiento_inválido(Exception):
    """
    Excepción que se lanza cuando un movimiento no es válido según las reglas del juego.

    Atributos:
        __mensaje__ (str): Mensaje de error que describe el motivo por el cual el movimiento no es válido.
    """
    def __init__(self, mensaje="El movimiento no es válido"):
        """
        Inicializa la excepción con un mensaje de error.

        Args:
            mensaje (str): Mensaje que describe el error. Por defecto, "El movimiento no es válido".
        """
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        """
        Devuelve una representación en cadena del mensaje de error.

        Returns:
            str: El mensaje de error.
        """
        return self.__mensaje__


class turno_invalido(Exception):
    """
    Excepción que se lanza cuando un jugador intenta mover una pieza en el turno equivocado.

    Atributos:
        __mensaje__ (str): Mensaje de error que describe la infracción de turno.
    """
    def __init__(self, mensaje="El turno no es válido"):
        """
        Inicializa la excepción con un mensaje de error.

        Args:
            mensaje (str): Mensaje que describe el error. Por defecto, "El turno no es válido".
        """
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        """
        Devuelve una representación en cadena del mensaje de error.

        Returns:
            str: El mensaje de error.
        """
        return self.__mensaje__


class fuera_del_tablero(Exception):
    """
    Excepción que se lanza cuando se intenta acceder a una posición fuera de los límites del tablero.

    Atributos:
        __mensaje__ (str): Mensaje de error que describe el problema de la posición fuera del tablero.
    """
    def __init__(self, mensaje="La posición indicada se encuentra fuera del tablero"):
        """
        Inicializa la excepción con un mensaje de error.

        Args:
            mensaje (str): Mensaje que describe el error. Por defecto, "La posición indicada se encuentra fuera del tablero".
        """
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        """
        Devuelve una representación en cadena del mensaje de error.

        Returns:
            str: El mensaje de error.
        """
        return self.__mensaje__


class movimiento_sin_pieza(Exception):
    """
    Excepción que se lanza cuando se intenta mover una pieza desde una posición vacía.

    Atributos:
        __mensaje__ (str): Mensaje de error que describe la situación de un movimiento sin pieza.
    """
    def __init__(self, mensaje="Movimiento sin pieza"):
        """
        Inicializa la excepción con un mensaje de error.

        Args:
            mensaje (str): Mensaje que describe el error. Por defecto, "Movimiento sin pieza".
        """
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        """
        Devuelve una representación en cadena del mensaje de error.

        Returns:
            str: El mensaje de error.
        """
        return self.__mensaje__
