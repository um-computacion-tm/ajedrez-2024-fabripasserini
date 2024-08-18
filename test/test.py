import sys
import os
import unittest

# Añadir el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chess.tablero import Tablero

class TestTablero(unittest.TestCase):
    
    def test_inicializacion(self):
        tablero = Tablero()
        self.assertIsNotNone(tablero)  # Verifica que el objeto Tablero se inicializa correctamente

if __name__ == '__main__':
    unittest.main()

