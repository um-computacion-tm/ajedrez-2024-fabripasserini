class movimiento_inválido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.__mensaje__ = "El movimiento no es válido"

    def __str__(self):
        return self.__mensaje__

class turno_invalido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.__mensaje__ = "El turno no es válido"

    def __str__(self):
        return self.__mensaje__
    
class fuera_del_tablero(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.__mensaje__ = "La posicion indicada se encuentra fuera del tablero"

    def __str__(self):
        return self.__mensaje__

class movimiento_sin_pieza(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.__mensaje__ = "Movimiento sin pieza"

    def __str__(self):
        return self.__mensaje__