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

    def setUp(self):
        # Inicializa un tablero vacío para cada prueba
        self.tablero = Tablero()
        self.peon_blanco = Peon("BLANCO", self.tablero)
        self.peon_negro = Peon("NEGRO", self.tablero)

    def test_obtener_posiciones_mover_peon_blanco_inicial(self):
        posiciones = self.peon_blanco.obtener_posiciones_mover(6, 3)  
        self.assertIn((5, 3), posiciones)  
        self.assertIn((4, 3), posiciones)  

    def test_obtener_posiciones_mover_peon_negro_inicial(self):
        posiciones = self.peon_negro.obtener_posiciones_mover(1, 3)  
        self.assertIn((2, 3), posiciones)  
        self.assertIn((3, 3), posiciones)  

    
if __name__ == '__main__':
    unittest.main()