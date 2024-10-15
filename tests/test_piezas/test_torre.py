import unittest
from chess.tablero import Tablero
from chess.piezas.torre import Torre
from chess.excepciones import movimiento_inválido, fuera_del_tablero

class TestTorre(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()
        self.torre_blanca = Torre("BLANCO", self.tablero)
        self.torre_negra = Torre("NEGRO", self.tablero)
        self.tablero.vaciar_tablero()  # Limpiamos el tablero de piezas
 
    

    def test_obtener_posiciones_verticales_negro(self):
        self.tablero.vaciar_tablero() 
        self.tablero.poner_pieza(1, 4, self.torre_negra) # Limpiamos el tablero de piezas
        posiciones = self.torre_negra.obtener_posiciones_verticales(1, 4)
        self.assertIn((3, 4), posiciones)
        self.assertIn((4, 4), posiciones)
        self.assertIn((5, 4), posiciones)
        self.assertIn((6, 4), posiciones)
        self.assertIn((2, 4), posiciones)
        

    def test_obtener_posiciones_horizontales_blanco(self):
        self.tablero.poner_pieza(4, 4, self.torre_blanca)
        posiciones = self.torre_blanca.obtener_posiciones_horizontales(4, 4)
        self.assertIn((4, 5), posiciones)
        self.assertIn((4, 6), posiciones)
        self.assertIn((4, 7), posiciones)
        self.assertIn((4, 3), posiciones)
        self.assertIn((4, 2), posiciones)
        self.assertIn((4, 1), posiciones)
        self.assertIn((4, 0), posiciones)

    def test_movimiento_bloqueado_vertical(self):
        otra_torre = Torre("NEGRO", self.tablero)
        self.tablero.poner_pieza(4, 4, otra_torre)
        self.tablero.poner_pieza(5, 4, self.torre_negra)
        posiciones = self.torre_negra.obtener_posiciones_verticales(5, 4)
        self.assertNotIn((4, 4), posiciones)  # No debería poder moverse a (4, 4)

    def test_movimiento_bloqueado_horizontal(self):
        otra_torre = Torre("NEGRO", self.tablero)
        self.tablero.poner_pieza(4, 6, otra_torre)
        self.tablero.poner_pieza(4, 4, self.torre_negra)
        posiciones = self.torre_negra.obtener_posiciones_horizontales(4, 4)
        self.assertNotIn((4, 6), posiciones)  # No debería poder moverse a (4, 6)

    def test_fuera_del_tablero(self):
        with self.assertRaises(fuera_del_tablero):
            self.torre_blanca.es_posicion_valida(8, 4)

    def test_captura_enemiga_vertical(self):
        otra_torre = Torre("NEGRO", self.tablero)
        self.tablero.poner_pieza(3, 4, otra_torre)
        self.tablero.poner_pieza(5, 4, self.torre_blanca)
        posiciones = self.torre_blanca.obtener_posiciones_verticales(5, 4)
        self.assertIn((3, 4), posiciones)  # Debería poder capturar la torre negra

    def test_captura_enemiga_horizontal(self):
        otra_torre = Torre("NEGRO", self.tablero)
        self.tablero.poner_pieza(4, 6, otra_torre)
        self.tablero.poner_pieza(4, 4, self.torre_blanca)
        posiciones = self.torre_blanca.obtener_posiciones_horizontales(4, 4)
        self.assertIn((4, 6), posiciones)  # Debería poder capturar la torre negra

if __name__ == '__main__':
    unittest.main()
