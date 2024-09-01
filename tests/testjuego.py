import unittest
from chess.piezas.pieza import Pieza
from chess.tablero import Tablero

class TestPieza(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()  
        self.pieza_blanca = Pieza('blanco', self.tablero)
        self.pieza_negra = Pieza('negro', self.tablero)

    def test_color_pieza(self):
        self.assertEqual(self.pieza_blanca.__color__, 'blanco')
        self.assertEqual(self.pieza_negra.__color__, 'negro')

if __name__ == '__main__':
    unittest.main()
