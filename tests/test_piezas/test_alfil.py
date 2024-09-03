import unittest
from chess.piezas.alfil import Alfil
from chess.tablero import Tablero

class TestAlfil(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        alfil = Alfil("BLANCO", tablero)
        self.assertEqual(
            str(alfil),
            "♝",
        )

if __name__ == '__main__':
    unittest.main()