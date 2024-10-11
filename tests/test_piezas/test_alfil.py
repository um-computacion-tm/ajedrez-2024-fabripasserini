import unittest
from chess.piezas.alfil import Alfil
from chess.tablero import Tablero
from chess.excepciones import movimiento_inválido, fuera_del_tablero

class TestAlfil(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        alfil = Alfil("BLANCO", tablero)
        self.assertEqual(
            str(alfil),
            "♝",
        )  

    def setUp(self):
        self.tablero = Tablero()
        self.alfil_blanco = Alfil("BLANCO", self.tablero)
        self.alfil_negro = Alfil("NEGRO", self.tablero)

    def test_obtener_posiciones_mover_libre(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)
        # Diagonales libres sin obstrucciones
        self.assertIn((3, 3), posiciones)
        self.assertIn((2, 2), posiciones)
        self.assertIn((5, 5), posiciones)
        self.assertIn((6, 6), posiciones)

    def test_obtener_posiciones_mover_bloqueado(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        otra_pieza = Alfil("BLANCO", self.tablero)
        self.tablero.poner_pieza(3, 3, otra_pieza)  # Bloquea el alfil
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)
        self.assertNotIn((2, 2), posiciones)  # No puede avanzar más allá de (3, 3)
        self.assertIn((3, 3), posiciones)  # Puede llegar hasta (3, 3), pero no pasarla

    def test_movimiento_invalido_misma_pieza(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        otra_alfil_blanco = Alfil("BLANCO", self.tablero)
        self.tablero.poner_pieza(5, 5, otra_alfil_blanco)
        with self.assertRaises(movimiento_inválido):
            self.alfil_blanco.obtener_posiciones_mover(4, 4)  # Intento de moverse a una casilla ocupada

    def test_obtener_posiciones_comer(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        self.tablero.poner_pieza(5, 5, self.alfil_negro)  # Posiciona una pieza negra para capturar
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)
        self.assertIn((5, 5), posiciones)  # El alfil debe poder capturar en (5, 5)

    def test_fuera_del_tablero(self):
        with self.assertRaises(fuera_del_tablero):
            self.alfil_blanco.es_posicion_valida(8, 8)  # Verificamos que no puede moverse fuera del tablero

    def test_no_puede_saltar_pieza(self):
        self.tablero.poner_pieza(4, 4, self.alfil_blanco)
        self.tablero.poner_pieza(5, 5, self.alfil_negro)  # Obstrucción
        self.tablero.poner_pieza(6, 6, self.alfil_negro)  # Más adelante
        posiciones = self.alfil_blanco.obtener_posiciones_mover(4, 4)
        self.assertIn((5, 5), posiciones)  # Puede llegar hasta la primera pieza
        self.assertNotIn((6, 6), posiciones)

if __name__ == '__main__':
    unittest.main()