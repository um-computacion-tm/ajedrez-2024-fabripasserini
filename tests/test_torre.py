import unittest
from chess.piezas.torre import Torre
from chess.excepciones import *


class TableroMock:
    def __init__(self):
        self.tablero = [[None for _ in range(8)] for _ in range(8)]

    def obtener_pieza(self, fila, columna):
        if 0 <= fila < 8 and 0 <= columna < 8:
            return self.tablero[fila][columna]
        return None

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.tablero = TableroMock()
        self.torre_blanca = Torre("BLANCO", self.tablero)
        self.torre_negra = Torre("NEGRO", self.tablero)

    def test_obtener_posibles_posiciones(self):
        # Posiciones válidas en línea recta sin obstáculos
        self.tablero.tablero[3][1] = None
        self.tablero.tablero[5][1] = None
        self.assertIn((3, 1), self.torre_blanca.obtener_posibles_posiciones(4, 1))
        self.assertIn((5, 1), self.torre_blanca.obtener_posibles_posiciones(4, 1))
        
        # Colocar una pieza del mismo color en el camino
        self.tablero.tablero[2][1] = Torre("BLANCO", self.tablero)
        self.assertNotIn((2, 1), self.torre_blanca.obtener_posibles_posiciones(4, 1))

        # Colocar una pieza del color contrario
        self.tablero.tablero[3][1] = Torre("NEGRO", self.tablero)
        self.assertIn((3, 1), self.torre_blanca.obtener_posibles_posiciones(4, 1))

    def test_es_casilla_vacia(self):
        # Test para verificar si una casilla está vacía
        self.assertTrue(self.torre_blanca.es_casilla_vacia(0, 0))  # Debe estar vacía
        self.tablero.tablero[0][0] = Torre("NEGRO", self.tablero)  # Colocar pieza
        self.assertFalse(self.torre_blanca.es_casilla_vacia(0, 0))  # No debe estar vacía

    def test_es_posicion_valida(self):
        # Test para posiciones válidas
        self.assertTrue(self.torre_blanca.es_posicion_valida(0, 0))
        self.assertTrue(self.torre_blanca.es_posicion_valida(7, 7))
        
        # Probar posiciones fuera de límites
        with self.assertRaises(fuera_del_tablero):
            self.torre_blanca.es_posicion_valida(8, 8)
        with self.assertRaises(fuera_del_tablero):
            self.torre_blanca.es_posicion_valida(-1, -1)

    def test_obtener_posiciones_verticales(self):
        # Test para obtener posiciones verticales
        self.tablero.tablero[3][1] = None
        self.tablero.tablero[5][1] = None
        self.assertIn((3, 1), self.torre_blanca.obtener_posiciones_verticales(4, 1))
        self.assertIn((5, 1), self.torre_blanca.obtener_posiciones_verticales(4, 1))
        
        # Colocar una pieza del mismo color
        self.tablero.tablero[2][1] = Torre("BLANCO", self.tablero)
        self.assertNotIn((2, 1), self.torre_blanca.obtener_posiciones_verticales(4, 1))

        # Colocar una pieza del color contrario
        self.tablero.tablero[3][1] = Torre("NEGRO", self.tablero)
        self.assertIn((3, 1), self.torre_blanca.obtener_posiciones_verticales(4, 1))

    def test_obtener_posiciones_horizontales(self):
        # Test para obtener posiciones horizontales
        self.tablero.tablero[1][3] = None
        self.tablero.tablero[1][5] = None
        self.assertIn((1, 3), self.torre_blanca.obtener_posiciones_horizontales(1, 4))
        self.assertIn((1, 5), self.torre_blanca.obtener_posiciones_horizontales(1, 4))
        
        # Colocar una pieza del mismo color
        self.tablero.tablero[1][2] = Torre("BLANCO", self.tablero)
        self.assertNotIn((1, 2), self.torre_blanca.obtener_posiciones_horizontales(1, 4))

        # Colocar una pieza del color contrario
        self.tablero.tablero[1][3] = Torre("NEGRO", self.tablero)
        self.assertIn((1, 3), self.torre_blanca.obtener_posiciones_horizontales(1, 4))

    def test_obtener_posiciones_en_direccion(self):
        # Test para obtener posiciones en una dirección específica
        self.assertIn((2, 1), self.torre_blanca.obtener_posiciones_en_direccion(1, 1, 1, 0))  # Hacia abajo
        self.assertIn((0, 1), self.torre_blanca.obtener_posiciones_en_direccion(1, 1, -1, 0))  # Hacia arriba
        self.assertIn((1, 2), self.torre_blanca.obtener_posiciones_en_direccion(1, 1, 0, 1))  # Hacia derecha
        self.assertIn((1, 0), self.torre_blanca.obtener_posiciones_en_direccion(1, 1, 0, -1))  # Hacia izquierda


if __name__ == '__main__':
    unittest.main()


