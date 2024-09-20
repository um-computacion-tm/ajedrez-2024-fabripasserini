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

        posibles = peon.obtener_posibles_posiciones(1, 5)
        self.assertEqual(
            posibles,
            [(2, 5), (3, 5)]
        )

    def test_not_initial_black(self):
        tablero = Tablero()
        peon = Peon("NEGRO", tablero)

        posibles = peon.obtener_posibles_posiciones(2, 5)
        self.assertEqual(
            posibles,
            [(3, 5)]
        )


    def test_initial_white(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)

        posibles = peon.obtener_posibles_posiciones(6, 4)
        self.assertEqual(
            posibles,
            [(5, 4), (4, 4)]
        )

    def test_not_initial_white(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)

        posibles = peon.obtener_posibles_posiciones(5, 4)
        self.assertEqual(
            posibles,
            [(4, 4)]
        )

    def test_not_initial_white_block(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)
        tablero.poner_pieza(4, 4, Peon("NEGRO", tablero))

        posibles = peon.obtener_posibles_posiciones(5, 4)
        self.assertEqual(
            posibles,
            []
        )

    def test_not_initial_black_block(self):
        tablero = Tablero()
        peon = Peon("NEGRO", tablero)
        tablero.poner_pieza(5, 4, Peon("NEGRO", tablero))

        posibles = peon.obtener_posibles_posiciones(4, 4)
        self.assertEqual(
            posibles,
            []
        )
    

if __name__ == '__main__':
    unittest.main()
