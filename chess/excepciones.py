class movimiento_inválido(Exception):
    def __init__(self, mensaje="El movimiento no es válido"):
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        return self.__mensaje__

class turno_invalido(Exception):
    def __init__(self, mensaje="El turno no es válido"):
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        return self.__mensaje__

class fuera_del_tablero(Exception):
    def __init__(self, mensaje="La posicion indicada se encuentra fuera del tablero"):
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        return self.__mensaje__

class movimiento_sin_pieza(Exception):
    def __init__(self, mensaje="Movimiento sin pieza"):
        super().__init__(mensaje)
        self.__mensaje__ = mensaje

    def __str__(self):
        return self.__mensaje__
