import unittest
from chess.tablero import Tablero
from chess.piezas.torre import Torre
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon

class TestTablero(unittest.TestCase):
    def test_str_board(self):
        tablero = Tablero()
        self.assertEqual(
            str(tablero),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♛♚♝♞♜\n"
            )
        )

if __name__ == '__main__':
    unittest.main()


