import unittest
from chess.tablero import Tablero
from chess.piezas.pieza import Pieza
from chess.piezas.torre import Torre

class TestPieza(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()  # Crear un tablero para las pruebas
        self.pieza_blanca = Pieza("BLANCO", self.tablero)
        self.pieza_negra = Pieza("NEGRO", self.tablero)

    def test_inicializacion(self):
        self.assertEqual(self.pieza_blanca.obtener_color(), "BLANCO")
        self.assertEqual(self.pieza_negra.obtener_color(), "NEGRO")

    

    
if __name__ == '__main__':
    unittest.main()
