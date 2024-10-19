import unittest
from unittest.mock import patch
from chess.main import Ajedrez
from chess.juego import menu  # Asegúrate de que 'menu' esté importado correctamente

class TestAjedrezMenu(unittest.TestCase):  
    def setUp(self):
        self.chess = Ajedrez()  # Inicializamos el objeto 'chess'

    @patch('builtins.input', side_effect=['2'])  # Simulamos la entrada de opción '2'
    def test_opcion_salir(self, mock_input):
        # Llamamos al menú
        menu(self.chess)
        
        # Verificamos que la partida se haya terminado
        self.assertTrue(self.chess.__terminar_partida__)

if __name__ == "__main__":
    unittest.main()
