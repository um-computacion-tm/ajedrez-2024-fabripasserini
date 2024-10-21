import unittest
from chess.piezas.peon import Peon
from chess.tablero import Tablero
from chess.excepciones import movimiento_inválido, fuera_del_tablero

class TestPeon(unittest.TestCase):

    # Test para verificar la representación en cadena del peón
    def test_str(self):
        tablero = Tablero()
        peon = Peon("BLANCO", tablero)
        # Verifica que la representación del peón es la correcta
        self.assertEqual(
            str(peon),
            "♟",
        )

    # Configuración previa a cada test
    def setUp(self):
        self.tablero = Tablero()
        self.peon_blanco = Peon("BLANCO", self.tablero)
        self.peon_negro1 = Peon("NEGRO", self.tablero)

    # Test para el movimiento simple hacia adelante de un peón blanco
    def test_obtener_posicion_simple_blanco(self):
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posicion_simple(6, 4, -1)
        # Verifica que el peón puede moverse una casilla hacia adelante
        self.assertIn((5, 4), posiciones)

    # Test para el movimiento simple hacia adelante de un peón negro
    def test_obtener_posicion_simple_negro(self):
        self.tablero.poner_pieza(1, 4, self.peon_negro1)
        posiciones = self.peon_negro1.obtener_posicion_simple(1, 4, 1)
        # Verifica que el peón negro puede moverse una casilla hacia adelante
        self.assertIn((2, 4), posiciones)

    # Test para el movimiento inicial doble de un peón blanco
    def test_obtener_posicion_inicial_doble_blanco(self):
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posicion_inicial_doble(6, 4, -1, 6)
        # Verifica que el peón puede moverse dos casillas en su primer movimiento
        self.assertIn((4, 4), posiciones)

    # Test para el movimiento inicial doble de un peón negro
    def test_obtener_posicion_inicial_doble_negro(self):
        self.tablero.poner_pieza(1, 4, self.peon_negro1)
        posiciones = self.peon_negro1.obtener_posicion_inicial_doble(1, 4, 1, 1)
        # Verifica que el peón negro puede moverse dos casillas en su primer movimiento
        self.assertIn((3, 4), posiciones)

    # Test para verificar que un peón no puede moverse si hay una pieza delante bloqueándolo
    def test_movimiento_bloqueado(self):
        otra_peon = Peon("NEGRO", self.tablero)
        self.tablero.poner_pieza(5, 4, otra_peon)
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        # Verifica que se lanza una excepción si el movimiento está bloqueado
        with self.assertRaises(movimiento_inválido):
            self.peon_blanco.obtener_posicion_simple(6, 4, -1)

    # Test para verificar que un peón no puede moverse fuera del tablero
    def test_fuera_del_tablero(self):
        # Verifica que se lanza una excepción cuando se intenta mover fuera del tablero
        with self.assertRaises(fuera_del_tablero):
            self.peon_blanco.es_posicion_valida(8, 4)

    # Test para verificar que un peón blanco puede capturar en diagonal
    def test_obtener_posibles_comer_blanco(self):
        self.tablero.poner_pieza(5, 3, Peon("NEGRO", self.tablero))
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posibles_comer(6, 4)
        # Verifica que el peón puede capturar la pieza enemiga en (5, 3)
        self.assertIn((5, 3), posiciones)

    # Test para obtener las posiciones válidas de movimiento para un peón blanco
    def test_obtener_posiciones_mover_blanco(self):
        self.tablero.poner_pieza(6, 4, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posiciones_mover(6, 4)
        # Verifica que el peón puede moverse una o dos casillas hacia adelante
        self.assertIn((5, 4), posiciones)
        self.assertIn((4, 4), posiciones)

    # Test para obtener las posiciones válidas de movimiento para un peón negro
    def test_obtener_posiciones_mover_negro(self):
        self.tablero.poner_pieza(1, 4, self.peon_negro1)
        posiciones = self.peon_negro1.obtener_posiciones_mover(1, 4)
        # Verifica que el peón negro puede moverse una o dos casillas hacia adelante
        self.assertIn((2, 4), posiciones)
        self.assertIn((3, 4), posiciones)

    # Test para verificar el movimiento de un peón blanco en la esquina superior izquierda del tablero
    def test_peon_blanco_esquina_superior_izquierda(self):
        self.tablero.poner_pieza(6, 0, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posiciones_mover(6, 0)
        # Verifica que el peón puede moverse hacia adelante
        self.assertIn((5, 0), posiciones)
        self.assertIn((4, 0), posiciones)

    # Test para verificar el movimiento de un peón negro en la esquina inferior izquierda del tablero
    def test_peon_negro_esquina_inferior_izquierda(self):
        self.tablero.poner_pieza(1, 0, self.peon_negro1)
        posiciones = self.peon_negro1.obtener_posiciones_mover(1, 0)
        # Verifica que el peón puede moverse hacia adelante
        self.assertIn((2, 0), posiciones)
        self.assertIn((3, 0), posiciones)

    # Test para verificar el movimiento de un peón blanco en la esquina superior derecha del tablero
    def test_peon_blanco_esquina_superior_derecha(self):
        self.tablero.poner_pieza(6, 7, self.peon_blanco)
        posiciones = self.peon_blanco.obtener_posiciones_mover(6, 7)
        # Verifica que el peón puede moverse hacia adelante
        self.assertIn((5, 7), posiciones)
        self.assertIn((4, 7), posiciones)

    # Test para verificar el movimiento de un peón negro en la esquina inferior derecha del tablero
    def test_peon_negro_esquina_inferior_derecha(self):
        self.tablero.poner_pieza(1, 7, self.peon_negro1)
        posiciones = self.peon_negro1.obtener_posiciones_mover(1, 7)
        # Verifica que el peón puede moverse hacia adelante
        self.assertIn((2, 7), posiciones)
        self.assertIn((3, 7), posiciones)

if __name__ == '__main__':
    unittest.main()
