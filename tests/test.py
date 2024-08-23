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
    
    def test_mover_pieza_fuera_del_tablero(self):
        """Prueba que mover una pieza fuera del tablero lanza un ValueError"""
        with self.assertRaises(ValueError):
            self.tablero.mover_pieza(-1, 0, 3, 0)  # Coordenada de origen fuera del rango

        with self.assertRaises(ValueError):
            self.tablero.mover_pieza(1, 0, 8, 0)  # Coordenada de destino fuera del rango

        with self.assertRaises(ValueError):
            self.tablero.mover_pieza(1, 8, 3, 0)  # Coordenada de origen fuera del rango

        with self.assertRaises(ValueError):
            self.tablero.mover_pieza(1, 0, 3, 8)

if __name__ == '__main__':
    unittest.main()
