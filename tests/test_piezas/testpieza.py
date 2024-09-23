import unittest
from chess.tablero import Tablero
from chess.piezas.pieza import Pieza
from chess.piezas.torre import Torre

class TestPieza(unittest.TestCase):
    def setUp(self):
        self.tablero_real = Tablero()
        self.pieza_blanca = Pieza("BLANCO", self.tablero_real)
        self.pieza_negra = Pieza("NEGRO", self.tablero_real)

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

    def test_obtener_color(self):
        self.assertEqual(self.pieza_blanca.obtener_color(), "BLANCO")
        self.assertEqual(self.pieza_negra.obtener_color(), "NEGRO")

    def test_posibles_posiciones_vd_sin_bloqueo(self):
        posiciones = self.pieza_blanca.posibles_posiciones_vd(3, 3)
        esperado = [(4, 3), (5, 3)]
        self.assertEqual(posiciones, esperado)

    def test_mover(self):
        tablero = Tablero()
        torre = Torre(color='NEGRO', tablero=tablero)
        tablero.poner_pieza(0, 0, torre)

        tablero.mover(
            desde_fila=0,
            desde_columna=0,
            hasta_fila=0,
            hasta_columna=1,
        )

        self.assertIsInstance(
            tablero.obtener_pieza(0, 1),
            Torre,
        )

if __name__ == '__main__':
    unittest.main()
