import unittest
from chess.piezas.pieza import Pieza
from chess.tablero import Tablero
from chess.juego import play
from unittest.mock import patch
from io import StringIO

class TestPieza(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()  
        self.pieza_blanca = Pieza('blanco', self.tablero)
        self.pieza_negra = Pieza('negro', self.tablero)

    def test_color_pieza(self):
        self.assertEqual(self.pieza_blanca.__color__, 'blanco')
        self.assertEqual(self.pieza_negra.__color__, 'negro')


class AjedrezMock:
    def __init__(self):
        self.turno = 'Blanco'
    
    def mostrar_tablero(self):
        return "tablero"

    def mover(self, desde_fila, desde_columna, hacia_fila, hacia_columna):
        # Simulamos un movimiento válido
        if desde_fila == 0 and desde_columna == 0 and hacia_fila == 1 and hacia_columna == 0:
            return True
        # Simulamos un movimiento inválido
        else:
            raise ValueError("Movimiento inválido")

class TestPlayFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['0', '0', '1', '0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_valid_move(self, mock_stdout, mock_input):
        ajedrez = AjedrezMock()
        play(ajedrez)
        output = mock_stdout.getvalue()
        self.assertIn("tablero", output)
        self.assertIn("turno:  Blanco", output)
        self.assertNotIn("error", output)

    @patch('builtins.input', side_effect=['0', '0', '2', '2'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_invalid_move(self, mock_stdout, mock_input):
        ajedrez = AjedrezMock()
        play(ajedrez)
        output = mock_stdout.getvalue()
        self.assertIn("tablero", output)
        self.assertIn("turno:  Blanco", output)
        self.assertIn("error Movimiento inválido", output)
 

if __name__ == '__main__':
    unittest.main()
