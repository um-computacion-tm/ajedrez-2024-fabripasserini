import unittest
from chess.tablero import Tablero
from chess.piezas.pieza import Pieza
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
    

    def test_poner_pieza_en_posicion_ocupada(self):
        tablero = Tablero()
        caballo_blanco = Caballo('blanco', tablero)
        tablero.poner_pieza(0, 0, caballo_blanco)
        pieza = tablero.obtener_pieza(0, 0)
        self.assertEqual(str(pieza), "♘")

class TestMoverPieza(unittest.TestCase):  # Asegúrate de que el nombre de la clase sea correcto
    def setUp(self):
        # Inicializa el tablero antes de cada test
        self.tablero = Tablero()

    def test_mover_pieza(self):
        pieza = Pieza('blanco', self.tablero)  
        self.tablero.poner_pieza(0, 0, pieza)  

        self.tablero.mover(0, 0, 0, 1)

        self.assertIsNone(self.tablero.obtener_pieza(0, 0))
        
        self.assertEqual(self.tablero.obtener_pieza(0, 1), pieza)

if __name__ == '__main__':
    unittest.main()


