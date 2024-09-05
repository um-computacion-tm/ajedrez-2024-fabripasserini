class movimiento_inválido(Exception):
    mensaje = "El movimiento no es válido"
    def __str__(self):
        return self

class movimiento_sin_pieza(Exception):
    mensaje = "La posicion se encuentra vacía"
    def __str__(self):
        return self

class turno_invalido(Exception):
    mensaje = "El turno no es válido"
    def __str__(self):
        return self
    
class fuera_del_tablero(Exception):
    mensaje = "La posicion indicada se encuentra fuera del tablero"
    def __str__(self):
        return self
