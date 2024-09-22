import unittest
from chess.piezas.torre import Torre
from chess.tablero import Tablero
from chess.piezas.peon import Peon

class TestTorre(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        torre = Torre("BLANCO", tablero)
        self.assertEqual(
            str(torre),
            "♜",
        )

    def test_mover_vertical_asc(self):
        tablero = Tablero()
        torre = Torre("BLANCO", tablero)
        posibles = torre.posibles_posiciones_va(4, 1)
        self.assertEqual(
            posibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        tablero = Tablero()
        tablero.poner_pieza(6, 1, Peon("BLANCO", tablero))
        torre = Torre("BLANCO", tablero)
        tablero.poner_pieza(4, 1, torre)
        possibles = torre.posibles_posiciones_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

   
        
if __name__ == '__main__':
    unittest.main()