import unittest
from chess.piezas.peon import Peon
from chess.tablero import Tablero
from chess.excepciones import movimiento_inválido, fuera_del_tablero

class TestPeon(unittest.TestCase):

    def test_str(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)
        self.assertEqual(
            str(peon),
            "♟",
        )

    def setUp(self):
        self.tablero = Tablero()
        self.peon_blanco = Peon("BLANCO", self.tablero)
        self.peon_negro = Peon("NEGRO", self.tablero)

    def test_obtener_posicion_simple_blanco(self):
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posicion_simple(6, 4, -1)
        self.assertIn((5, 4), posiciones)

    def test_obtener_posicion_simple_negro(self):
        self.tablero.poner_pieza(1, 4, self.peon_negro)
        posiciones = self.peon_negro.obtener_posicion_simple(1, 4, 1)
        self.assertIn((2, 4), posiciones)
    
    def test_obtener_posicion_inicial_doble_blanco(self):
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posicion_inicial_doble(6, 4, -1, 6)
        self.assertIn((4, 4), posiciones)

    def test_obtener_posicion_inicial_doble_negro(self):
        self.tablero.poner_pieza(1, 4, self.peon_negro)
        posiciones = self.peon_negro.obtener_posicion_inicial_doble(1, 4, 1, 1)
        self.assertIn((3, 4), posiciones)
    
    def test_movimiento_bloqueado(self):
        otra_peon = Peon("NEGRO", self.tablero)
        self.tablero.poner_pieza(5, 4, otra_peon)
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        with self.assertRaises(movimiento_inválido):
            self.peon_blanco.obtener_posicion_simple(6, 4, -1)

    def test_fuera_del_tablero(self):
        with self.assertRaises(fuera_del_tablero):
            self.peon_blanco.es_posicion_valida(8, 4)
    
    def test_obtener_posibles_comer_blanco(self):
        self.tablero.poner_pieza(5, 3, Peon("NEGRO", self.tablero))
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posibles_comer(6, 4)
        self.assertIn((5, 3), posiciones)

    def test_no_puede_comer_pieza_propia(self):
        self.tablero.poner_pieza(5, 3, Peon("BLANCO", self.tablero))
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        with self.assertRaises(movimiento_inválido):
            self.peon_blanco.obtener_posibles_comer(6, 4)
    
    def test_obtener_posiciones_mover_blanco(self):
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posiciones_mover(6, 4)
        self.assertIn((5, 4), posiciones)
        self.assertIn((4, 4), posiciones)

    def test_obtener_posiciones_mover_negro(self):
        self.tablero.poner_pieza(1, 4, self.peon_negro)
        posiciones = self.peon_negro.obtener_posiciones_mover(1, 4)
        self.assertIn((2, 4), posiciones)
        self.assertIn((3, 4), posiciones)
    
if __name__ == '__main__':
    unittest.main()