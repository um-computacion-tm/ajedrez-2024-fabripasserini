import unittest
from chess.piezas.caballo import Caballo
from chess.tablero import Tablero

class TestCaballo(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        caballo = Caballo("BLANCO", tablero)
        self.assertEqual(
            str(caballo),
            "♞",
        )

if __name__ == '__main__':
    unittest.main()