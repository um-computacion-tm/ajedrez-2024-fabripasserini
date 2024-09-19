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

    def test_initial_black(self):
        tablero = Tablero()
        peon = Peon("NEGRO", tablero)

        possibles = peon.obtener_posibles_posiciones(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )

    def test_not_initial_black(self):
        tablero = Tablero()
        peon = Peon("NEGRO", tablero)

        possibles = peon.obtener_posibles_posiciones(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )


    def test_initial_white(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)

        possibles = peon.obtener_posibles_posiciones(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

    

if __name__ == '__main__':
    unittest.main()
