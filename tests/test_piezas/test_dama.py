import unittest
from chess.piezas.dama import Dama
from chess.tablero import Tablero

class TestDama(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        dama = Dama("BLANCO", tablero)
        self.assertEqual(
            str(dama),
            "♜",
        )

if __name__ == '__main__':
    unittest.main()