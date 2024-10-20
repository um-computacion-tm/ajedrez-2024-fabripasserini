import unittest
from unittest.mock import patch
from chess.main import Ajedrez
from chess.juego import *  # Asegúrate de que 'menu' esté importado correctamente

class TestAjedrezMenu(unittest.TestCase):  
    def setUp(self):
        self.chess = Ajedrez()  

    @patch('builtins.input', side_effect=['2'])  
    def test_opcion_salir(self, mock_input):
        menu(self.chess)
        
        self.assertTrue(self.chess.__terminar_partida__)


    @patch('builtins.input', side_effect=['2'])
    def test_menu_juego_salir(self, mock_input):
        menu_juego(self.chess)
        self.assertTrue(self.chess.__terminar_partida__) 

    @patch('builtins.input', side_effect=['0', '0', '1', '1'])  
    def test_play_movimiento_valido(self, mock_input):
        with patch('chess.main.Ajedrez.mover_pieza') as mock_mover_pieza:
            play(self.chess)
            mock_mover_pieza.assert_called_once_with(0, 0, 1, 1)

    @patch('builtins.input', side_effect=['6', '6', '1', '1'])  
    def test_play_movimiento_invalido(self, mock_input):
        with patch('chess.main.Ajedrez.mover_pieza', side_effect= movimiento_inválido):
            with patch('builtins.print') as mock_print:
                play(self.chess)
                mock_print.assert_any_call('Invalid move: El movimiento no es válido')

if __name__ == "__main__":
    unittest.main()

