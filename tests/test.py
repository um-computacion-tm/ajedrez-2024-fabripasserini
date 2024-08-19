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



import unittest
from chess.pieza import pieza  # Asegúrate de que la importación es correcta según tu estructura de carpetas

class TestPieza(unittest.TestCase):
    def setUp(self):
        self.pieza = pieza('Reina', 'Blanco', 0, 3)

    def test_atributos(self):
        self.assertEqual(self.pieza.__nombre__, 'Reina')
        self.assertEqual(self.pieza.__color__, 'Blanco')
        self.assertEqual(self.pieza.__fila__, 0)
        self.assertEqual(self.pieza.__columna__, 3)

if __name__ == '__main__':
    unittest.main()
