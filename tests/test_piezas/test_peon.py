import unittest
from chess.piezas.peon import Peon
from chess.tablero import Tablero

class TestPeon(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)
        self.assertEqual(
            str(peon),
            "♟",
        )

if __name__ == '__main__':
    unittest.main()