import unittest
from unittest.mock import patch, MagicMock
from chess.main import Ajedrez
from chess.excepciones import *

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.ajedrez = Ajedrez()

    def test_iniciar_juego(self):
        self.assertTrue(self.ajedrez.en_juego())
        self.assertEqual(self.ajedrez.turnos(), "BLANCO")


    def test_cambiar_turno(self):
        self.ajedrez.cambiar_turno()
        self.assertEqual(self.ajedrez.turnos(), "NEGRO") 

if __name__ == "__main__":
    unittest.main()
