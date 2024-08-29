import unittest
from chess.tablero import Tablero
from chess.piezas.pieza import Pieza

class TestPieza(unittest.TestCase):
    def setUp(self):
        self.tablero_real = Tablero()

    def test_str_blanco(self):
        Pieza.blanco_str = "♜"
        Pieza.negro_str = "♖"
        pieza_blanca = Pieza("BLANCO", self.tablero_real)
        self.assertEqual(str(pieza_blanca), "♜")

    def test_str_negro(self):
        Pieza.blanco_str = "♜"
        Pieza.negro_str = "♖"
        pieza_negra = Pieza("NEGRO", self.tablero_real)
        self.assertEqual(str(pieza_negra), "♖")


if __name__ == '__main__':
    unittest.main()
