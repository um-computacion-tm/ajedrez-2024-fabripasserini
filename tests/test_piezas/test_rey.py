import unittest
from chess.piezas.rey import Rey
from chess.tablero import Tablero

class TestRey(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        rey = Rey("BLANCO", tablero)
        self.assertEqual(
            str(rey),
            "♚",
        )

if __name__ == '__main__':
    unittest.main()