import unittest
from chess.tablero import Tablero
from chess.piezas.pieza import Pieza
from chess.piezas.torre import Torre
from chess.piezas.rey import Rey
from chess.piezas.caballo import Caballo
from chess.piezas.alfil import Alfil
from chess.piezas.dama import Dama
from chess.piezas.peon import Peon
from chess.excepciones import fuera_del_tablero

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_inicializacion_tablero(self):
        # Verificar que las torres negras estén en la posición correcta
        self.assertIsInstance(self.tablero.obtener_pieza(0, 0), Torre)
        self.assertEqual(self.tablero.obtener_pieza(0, 0).obtener_color(), "NEGRO")
        self.assertIsInstance(self.tablero.obtener_pieza(0, 7), Torre)

        # Verificar que las piezas blancas estén en la posición inicial
        self.assertIsInstance(self.tablero.obtener_pieza(6, 0), Peon)
        self.assertEqual(self.tablero.obtener_pieza(6, 0).obtener_color(), "BLANCO")

    def test_obtener_pieza_fuera_del_tablero(self):
        # Verificar que se lanza una excepción al intentar obtener una pieza fuera del tablero
        with self.assertRaises(fuera_del_tablero):
            self.tablero.obtener_pieza(8, 8)

    def test_poner_pieza(self):
        # Verificar que se puede poner una pieza en una posición vacía
        nuevo_peon = Peon("BLANCO", self.tablero)
        self.tablero.poner_pieza(4, 4, nuevo_peon)
        self.assertEqual(self.tablero.obtener_pieza(4, 4), nuevo_peon)

    def test_imprimir_tablero(self):
        # No hay una manera directa de testear la impresión, pero podemos asegurarnos de que no haya errores.
        try:
            self.tablero.imprimir_tablero()
        except Exception as e:
            self.fail(f"imprimir_tablero lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()


