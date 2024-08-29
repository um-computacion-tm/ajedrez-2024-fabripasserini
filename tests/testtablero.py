import unittest
from chess.tablero import Tablero

class TestTablero(unittest.TestCase):

    def setUp(self):
    
        self.tablero = Tablero()
    
      
    def test_inicializacion(self):
        tablero = Tablero()
        self.assertIsNotNone(tablero)

    def test_mostrar_tablero(self):
        try:
            self.tablero.mostrar_tablero()
        except Exception as e:
            self.fail(f"mostrar_tablero lanzó una excepción: {e}")
    
   
if __name__ == '__main__':
    unittest.main()


