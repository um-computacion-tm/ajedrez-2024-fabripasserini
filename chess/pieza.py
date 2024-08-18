BLANCO='Blanco'
NEGRO='Negro'
diccionarioSimbolos = {
    BLANCO: {
        'Peon': "♙",
        'Torre': "♖",
        'Caballo': "♘",
        'Alfil': "♗",
        'Rey': "♔",
        'Dama': "♕"
    },
    NEGRO: {
        'Peon': "♟",
        'Torre': "♜",
        'Caballo': "♞",
        'Alfil': "♝",
        'Rey': "♚",
        'Dama': "♛"
    }
}

class pieza:
    def __init__(self, nombre, color, fila, columna):
        self.__nombre__ = nombre
        self.__color__ = color
        self.__fila__ = fila
        self.__columna__ = columna