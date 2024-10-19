import unittest
from unittest.mock import patch
from chess.juego import main


class TestAjedrezMenu(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', '2'])  # '1' para Jugar, '2' para Salir en el menú del juego
    def test_menu_jugar_y_salir(self, mock_input):
        main()


if __name__ == '__main__':
    unittest.main()

