import unittest
from chess.main import Ajedrez
from chess.tablero import Tablero

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.ajedrez = Ajedrez()

    def test_inicializacion(self):
        self.assertEqual(self.ajedrez.turno, "BLANCO", "El turno inicial debería ser 'BLANCO'")

    def test_mover_posicion_invalida(self):
        with self.assertRaises(ValueError):
            self.ajedrez.mover(-1, 0, 3, 0)  
        with self.assertRaises(ValueError):
            self.ajedrez.mover(0, 0, 8, 0) 


    def test_cambiar_turno(self):
        self.ajedrez.cambiar_turno()
        self.assertEqual(self.ajedrez.turno, "NEGRO", "Después de cambiar turno, debería ser 'NEGRO'")
        self.ajedrez.cambiar_turno()
        self.assertEqual(self.ajedrez.turno, "BLANCO", "Después de cambiar turno nuevamente, debería ser 'BLANCO'")

if __name__ == '__main__':
    unittest.main()
