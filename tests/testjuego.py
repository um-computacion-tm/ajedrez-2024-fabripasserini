import unittest
from unittest.mock import patch, MagicMock
from chess.juego import *
from chess.excepciones import movimiento_inválido


class TestAjedrezMain(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['2'])  # Simulamos que la opción es salir
    def test_menu_principal_salir(self, mock_input):
        chess_mock = MagicMock()
        chess_mock.__terminar_partida__ = False
        chess_mock.terminar_partida = MagicMock()
        
        menu(chess_mock)
        
        chess_mock.terminar_partida.assert_called_once()

    

    @patch('builtins.input', side_effect=['1','2'])  
    @patch('builtins.print')
    def test_main_menu_exit(self, mock_print, mock_input):
        chess = Ajedrez()
        menu(chess)
        mock_print.assert_any_call()
    


    @patch('builtins.input', side_effect=['1', '2', '3', '4']) 
    @patch('chess.main.Ajedrez.mostrar_tablero')  
    @patch('chess.main.Ajedrez.mover_pieza')  

    def test_play(self, mock_mover_pieza, mock_mostrar_tablero, mock_input):
        chess_mock = MagicMock()
        chess_mock.mover_pieza = MagicMock()

        play(chess_mock)
        
        chess_mock.mostrar_tablero.assert_called()
        chess_mock.mover_pieza.assert_called_with(1, 2, 3, 4)

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])  # Simular entradas
    @patch('chess.main.Ajedrez.mover_pieza', side_effect=movimiento_inválido('Movimiento inválido'))
    def test_play_movimiento_invalido(self, mock_mover_pieza, mock_input):
        chess_mock = MagicMock()
        
        with patch('builtins.print') as mock_print:
            play(chess_mock)
            mock_print.assert_any_call()




if __name__ == "__main__":
    unittest.main()

