import unittest
from chess.tablero import Tablero
from chess.piezas.torre import Torre
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon
from chess.excepciones import fuera_del_tablero

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
    
    def test_get_piece_out_of_range(self):
        tablero = Tablero()

        with self.assertRaises(fuera_del_tablero) as exc:
            tablero.obtener_pieza(10, 10)

        self.assertEqual(
            exc.exception.mensaje,
            "La posicion indicada se encuentra fuera del tablero"
        )

if __name__ == '__main__':
    unittest.main()


