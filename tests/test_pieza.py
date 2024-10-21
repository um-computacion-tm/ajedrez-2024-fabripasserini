import unittest
from chess.piezas.pieza import Pieza
from chess.excepciones import *

# Clase derivada de Pieza para realizar pruebas específicas
class PiezaTest(Pieza):
    # Definimos la representación de una pieza blanca y una negra
    blanco_str = "♙"  # Representación de una pieza blanca
    negro_str = "♟"   # Representación de una pieza negra

    # Método para obtener las posibles posiciones desde una posición dada
    def obtener_posibles_posiciones(self, desde_fila, desde_columna):
        posibles = []
        # Agregar solo posiciones válidas dentro del tablero
        if desde_fila + 1 < 8:  # Movimiento hacia abajo
            posibles.append((desde_fila + 1, desde_columna))
        if desde_fila - 1 >= 0:  # Movimiento hacia arriba
            posibles.append((desde_fila - 1, desde_columna))
        return posibles

# Clase de pruebas unitaria para la clase Pieza
class TestPieza(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de PiezaTest para realizar las pruebas
        self.pieza_blanca = PiezaTest("BLANCO", None)

    # Comprobamos que la inicialización de la pieza es correcta
    def test_inicializacion(self):
        self.assertEqual(self.pieza_blanca.obtener_color(), "BLANCO")

    # Verificamos que la representación de la pieza blanca es correcta
    def test_str_blanca(self):
        self.assertEqual(str(self.pieza_blanca), "♙")

    # Verificamos que la representación de la pieza negra es correcta
    def test_str_negra(self):
        pieza_negra = PiezaTest("NEGRO", None)
        self.assertEqual(str(pieza_negra), "♟")

    # Verificamos que las posiciones son válidas o no según las reglas
    def test_posiciones_validas(self):
        self.assertTrue(self.pieza_blanca.posiciones_validas(1, 1, 2, 1))  # Se espera True
        self.assertFalse(self.pieza_blanca.posiciones_validas(1, 1, 3, 1))  # Se espera False

    # Verificamos que se lanza la excepción NotImplementedError si el método no está implementado
    def test_obtener_posibles_posiciones(self):
        pieza_base = Pieza("BLANCO", None)
        with self.assertRaises(NotImplementedError):
            pieza_base.obtener_posibles_posiciones(0, 0)

    # Probamos la implementación del método obtener_posibles_posiciones en PiezaTest
    def test_obtener_posibles_posiciones_impl(self):
        self.assertIn((2, 1), self.pieza_blanca.obtener_posibles_posiciones(1, 1))  # Movimiento hacia abajo
        self.assertIn((0, 1), self.pieza_blanca.obtener_posibles_posiciones(1, 1))  # Movimiento hacia arriba
        self.assertNotIn((3, 1), self.pieza_blanca.obtener_posibles_posiciones(1, 1))  # No es un movimiento válido

# Ejecución del test
if __name__ == "__main__":
    unittest.main()

