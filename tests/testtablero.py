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

    def test_obtener_rey_blanco(self):
        tablero = Tablero()
        rey_blanco = tablero.obtener_rey_blanco()
        self.assertIsInstance(rey_blanco, Rey)
        self.assertEqual(rey_blanco.obtener_color(), "BLANCO")
    
    def test_obtener_rey_blanco_no_hay(self):
        tablero = Tablero(for_test=True)  # Sin piezas
        rey_blanco = tablero.obtener_rey_blanco()
        self.assertIsNone(rey_blanco)

    def test_obtener_rey_negro(self):
        tablero = Tablero()
        rey_negro = tablero.obtener_rey_negro()
        self.assertIsInstance(rey_negro, Rey)
        self.assertEqual(rey_negro.obtener_color(), "NEGRO")
    
    def test_obtener_rey_negro_no_hay(self):
        tablero = Tablero(for_test=True)  # Sin piezas
        rey_negro = tablero.obtener_rey_negro()
        self.assertIsNone(rey_negro)

    def test_cambiar_posiciones(self):
        tablero = Tablero(for_test=True)
        peon = Peon("BLANCO", tablero)
        tablero.poner_pieza(1, 1, peon)  # Poner un peón en (1, 1)
        tablero.cambiar_posiciones(1, 1, 3, 3)  # Mover el peón de (1, 1) a (3, 3)
        self.assertIsNone(tablero.obtener_pieza(1, 1))  # Debe estar vacío
        self.assertEqual(tablero.obtener_pieza(3, 3), peon) 

    def test_vaciar_tablero(self):
        # Crear un tablero con algunas piezas
        tablero = Tablero(for_test=True)
        peon = Peon("BLANCO", tablero)
        tablero.poner_pieza(1, 1, peon)  # Poner un peón en (1, 1)

        # Asegurarse de que el peón está en el tablero
        self.assertIsNotNone(tablero.obtener_pieza(1, 1))

        # Vaciar el tablero
        tablero.vaciar_tablero()

        # Verificar que todas las posiciones del tablero están vacías
        for fila in range(8):
            for columna in range(8):
                self.assertIsNone(tablero.obtener_pieza(fila, columna))


    def test_ganan_negras_sin_piezas_blancas(self):
        # Vaciar el tablero por completo antes de empezar
        self.tablero.vaciar_tablero()
        
        # Colocar solo piezas negras en el tablero
        peon_negro = Peon("NEGRO", self.tablero)
        self.tablero.poner_pieza(0, 0, peon_negro)
        
        # Verificar que el juego termina y las piezas negras ganan
        resultado = self.tablero.verificar_estado_juego()
        self.assertEqual(resultado, "NEGRO")

    def test_ganan_blancas_sin_piezas_negras(self):
        # Vaciar el tablero por completo antes de empezar
        self.tablero.vaciar_tablero()
        
        # Colocar solo piezas blancas en el tablero
        peon_blanco = Peon("BLANCO", self.tablero)
        self.tablero.poner_pieza(7, 7, peon_blanco)
        
        # Verificar que el juego termina y las piezas blancas ganan
        resultado = self.tablero.verificar_estado_juego()
        self.assertEqual(resultado, "BLANCO")

    def test_juego_continua_con_piezas_de_ambos_colores(self):
        # Colocar una pieza blanca y una pieza negra
        peon_blanco = Peon("BLANCO", self.tablero)
        peon_negro = Peon("NEGRO", self.tablero)
        self.tablero.poner_pieza(7, 7, peon_blanco)
        self.tablero.poner_pieza(0, 0, peon_negro)
        
        # Verificar que el juego continúa
        resultado = self.tablero.verificar_estado_juego()
        self.assertEqual(resultado, "CONTINUA")

if __name__ == '__main__':
    unittest.main()
