import unittest
from chess.piezas.torre import Torre
from chess.tablero import Tablero

class TestTorre(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        torre = Torre("BLANCO", tablero)
        self.assertEqual(
            str(torre),
            "♜",
        )

if __name__ == '__main__':
    unittest.main()
