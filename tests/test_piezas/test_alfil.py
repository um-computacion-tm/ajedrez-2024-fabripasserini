import unittest
from chess.piezas.alfil import Alfil
from chess.tablero import Tablero
from chess.excepciones import movimiento_inválido, fuera_del_tablero

class TestAlfil(unittest.TestCase):
    def test_str(self):
        tablero = Tablero()
        peon = Alfil("BLANCO", tablero)
        self.assertEqual(
            str(peon),
            "♝",
        )

    def setUp(self):
        # Configurar un tablero vacío y un alfil blanco
        self.tablero = Tablero()
        self.alfil_blanco = Alfil("BLANCO", self.tablero)
        self.alfil_negro = Alfil("NEGRO", self.tablero)
        self.tablero.vaciar_tablero()

    def test_movimiento_libre(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)

        self.assertIn((3, 3), posiciones)
        self.assertIn((2, 2), posiciones)
        self.assertIn((5, 5), posiciones)
        self.assertIn((3, 5), posiciones)
        self.assertIn((5, 3), posiciones)

    def test_movimiento_bloqueado_por_pieza_misma(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        self.tablero.poner_pieza(2, 2, self.alfil_blanco)
        
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)

        self.assertIn((3, 3), posiciones)
        self.assertNotIn((2, 2), posiciones)  

    def test_movimiento_con_captura(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        self.tablero.poner_pieza(2, 2, self.alfil_negro)
        
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)

        self.assertIn((2, 2), posiciones)
        self.assertNotIn((1, 1), posiciones)  

    def test_movimiento_fuera_del_tablero(self):
        self.tablero.poner_pieza(0, 0, self.alfil_blanco)
        posiciones = self.alfil_blanco.obtener_posiciones_mover(0, 0)

       
        self.assertIn((1, 1), posiciones)
        self.assertNotIn((-1, -1), posiciones)  

    

if __name__ == '__main__':
    unittest.main()
