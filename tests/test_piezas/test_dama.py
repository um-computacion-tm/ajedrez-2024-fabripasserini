import unittest
from chess.piezas.dama import Dama
from chess.tablero import Tablero

class TestDama(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        dama = Dama("BLANCO", tablero)
        self.assertEqual(
            str(dama),
            "♛",
        )

    
from chess.piezas.dama import Dama
from chess.tablero import Tablero
from chess.excepciones import fuera_del_tablero, movimiento_inválido

class TestDama(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
        self.dama_blanca = Dama("blanco", self.tablero)
        self.dama_negra = Dama("negro", self.tablero)
        self.tablero.poner_pieza(self.dama_blanca, 3, 3)  # Colocar la dama blanca en (3, 3)
        self.tablero.poner_pieza(self.dama_negra, 6, 6)  # Colocar la dama negra en (6, 6)

    def test_obtener_posibles_posiciones(self):
        # Test para las posibles posiciones de movimiento de la dama blanca
        posiciones = self.dama_blanca.obtener_posibles_posiciones(3, 3)
        self.assertIn((4, 4), posiciones)  # Movimiento diagonal
        self.assertIn((3, 4), posiciones)  # Movimiento horizontal
        self.assertIn((2, 3), posiciones)  # Movimiento vertical

    def test_es_posicion_valida_fuera_tablero(self):
        # Verificar si la excepción `fuera_del_tablero` es lanzada para una posición fuera del tablero
        with self.assertRaises(fuera_del_tablero):
            self.dama_blanca.es_posicion_valida(-1, -1)  # Posición inválida fuera del tablero

    def test_es_posicion_invalida_mismo_color(self):
        # Poner otra pieza blanca en una posición (4, 4)
        otra_dama_blanca = Dama("blanco", self.tablero)
        self.tablero.poner_pieza(otra_dama_blanca, 4, 4)
        with self.assertRaises(movimiento_inválido):
            self.dama_blanca.obtener_posiciones_diagonales(3, 3)  # Movimiento bloqueado por la pieza del mismo color

    def test_mover_captura(self):
        # Test para ver si la dama negra puede capturar a la dama blanca
        posiciones = self.dama_negra.obtener_posiciones_diagonales(6, 6)
        self.assertIn((3, 3), posiciones)  # Captura válida de la dama blanca


if __name__ == '__main__':
    unittest.main()