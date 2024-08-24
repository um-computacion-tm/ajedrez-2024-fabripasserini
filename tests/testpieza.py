import unittest
from chess.pieza import pieza
from chess.alfil import Alfil

class TestPieza(unittest.TestCase):
    def test_pieza_initialization(self):
        p1 = pieza('Rey', 'Blanco', 0, 4)
        
        self.assertEqual(p1.__nombre__, 'Rey')
        self.assertEqual(p1.__color__, 'Blanco')
        self.assertEqual(p1.__fila__, 0)
        self.assertEqual(p1.__columna__, 4)
    
def test_inicializacion_alfil():
    alfil_blanco = Alfil("BLANCO", 0, 2)
    assert alfil_blanco.nombre == "Alfil"
    assert alfil_blanco.color == "BLANCO"
    assert alfil_blanco.fila == 0
    assert alfil_blanco.columna == 2

    alfil_negro = Alfil("NEGRO", 7, 5)
    assert alfil_negro.nombre == "Alfil"
    assert alfil_negro.color == "NEGRO"
    assert alfil_negro.fila == 7
    assert alfil_negro.columna == 5


if __name__ == '__main__':
    unittest.main()