import unittest
from chess.piezas.alfil import Alfil
from chess.tablero import Tablero
from chess.excepciones import movimiento_inválido, fuera_del_tablero

class TestAlfil(unittest.TestCase):
    # comprobamos que funcione el método str
    def test_str(self):
        # Creamos un tablero y un alfil blanco
        tablero = Tablero()
        peon = Alfil("BLANCO", tablero)
        # Verificamos que la representación en cadena del alfil es la esperada
        self.assertEqual(
            str(peon),
            "♝",
        )

    def setUp(self):
        # Configurar un tablero vacío y un alfil blanco y negro
        self.tablero = Tablero()
        self.alfil_blanco = Alfil("BLANCO", self.tablero)
        self.alfil_negro = Alfil("NEGRO", self.tablero)
        self.tablero.vaciar_tablero()

    # Test para verificar que un alfil no puede moverse a través de piezas aliadas
    def test_movimiento_bloqueado_por_pieza_misma(self):
        # Colocamos el alfil blanco en (4, 4) y otro alfil blanco en (2, 2)
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        self.tablero.poner_pieza(2, 2, self.alfil_blanco)
        
        # Obtenemos las posiciones válidas de movimiento para el alfil en (4, 4)
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)

        # Verificamos que el alfil puede moverse a (3, 3) pero no a (2, 2)
        self.assertIn((3, 3), posiciones)
        self.assertNotIn((2, 2), posiciones)  

    # Test para verificar que el alfil puede capturar una pieza enemiga
    def test_movimiento_con_captura(self):
        # Colocamos el alfil blanco en (4, 4) y un alfil negro en (2, 2)
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        self.tablero.poner_pieza(2, 2, self.alfil_negro)
        
        # Obtenemos las posiciones válidas de movimiento para el alfil blanco
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)

        # Verificamos que el alfil puede capturar la pieza enemiga en (2, 2)
        self.assertIn((2, 2), posiciones)
        # Verificamos que no puede seguir avanzando a (1, 1) después de capturar
        self.assertNotIn((1, 1), posiciones)  

    # Test para verificar que el alfil no puede moverse fuera del tablero
    def test_movimiento_fuera_del_tablero(self):
        # Colocamos el alfil blanco en la esquina inferior izquierda (0, 0)
        self.tablero.poner_pieza(0, 0, self.alfil_blanco)
        posiciones = self.alfil_blanco.obtener_posiciones_mover(0, 0)

        # Verificamos que puede moverse a (1, 1) pero no fuera del tablero
        self.assertIn((1, 1), posiciones)
        self.assertNotIn((-1, -1), posiciones)  

    # Test para obtener todas las posiciones posibles de movimiento para un alfil
    def test_obtener_posibles_posiciones(self):
        # Colocamos el alfil blanco en la posición (2, 2)
        self.tablero.poner_pieza(2, 2, self.alfil_blanco)

        # Llamamos al método obtener_posibles_posiciones
        resultado = self.alfil_blanco.obtener_posibles_posiciones(2, 2)

        # Verificamos que el método devuelve las posiciones diagonales válidas
        self.assertIn((1, 1), resultado)
        self.assertIn((3, 3), resultado)
        self.assertIn((4, 4), resultado)
        self.assertIn((0, 0), resultado)

    # Test para verificar si una casilla está vacía
    def test_es_casilla_vacia(self):
        # Verificamos que una casilla vacía es detectada correctamente
        self.assertTrue(self.alfil_blanco.es_casilla_vacia(3, 3))

        # Colocamos una pieza en el tablero
        self.tablero.poner_pieza(3, 3, self.alfil_blanco)

        # Verificamos que la casilla ahora está ocupada
        self.assertFalse(self.alfil_blanco.es_casilla_vacia(3, 3))

    # Test para verificar si una posición es válida dentro del tablero
    def test_es_posicion_valida(self):
        # Verificamos que una posición dentro del tablero sea válida
        self.assertTrue(self.alfil_blanco.es_posicion_valida(3, 3))

        # Verificamos que una posición fuera del tablero lance la excepción
        with self.assertRaises(fuera_del_tablero):
            self.alfil_blanco.es_posicion_valida(8, 8)

    # Test para verificar las posiciones de movimiento del alfil
    def test_obtener_posiciones_mover(self):
        # Colocamos el alfil en la posición (4, 4)
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)

        # Verificamos que puede moverse en las cuatro direcciones diagonales
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)
        
        self.assertIn((3, 3), posiciones)  # Diagonal arriba izquierda
        self.assertIn((5, 5), posiciones)  # Diagonal abajo derecha
        self.assertIn((3, 5), posiciones)  # Diagonal arriba derecha
        self.assertIn((5, 3), posiciones)  # Diagonal abajo izquierda

        # Colocamos una pieza que bloquea el movimiento en (3, 3)
        otra_pieza = Alfil("negro", self.tablero)
        self.tablero.poner_pieza(3, 3, otra_pieza)

        # Verificamos que el alfil no puede pasar a través de la pieza enemiga
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)
        self.assertIn((3, 3), posiciones)  # Puede capturar la pieza
        self.assertNotIn((2, 2), posiciones)  # No puede saltar sobre la pieza

if __name__ == '__main__':
    unittest.main()
