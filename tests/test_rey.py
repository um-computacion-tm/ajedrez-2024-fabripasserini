import unittest
from chess.piezas.rey import Rey
from chess.piezas.peon import Peon
from chess.tablero import Tablero

class TestRey(unittest.TestCase):

    # Test para verificar la representación en cadena del rey
    def test_str(self):
        tablero = Tablero()
        rey = Rey("BLANCO", tablero)
        self.assertEqual(
            str(rey),
            "♚",  # Comprobamos que el símbolo para el rey blanco sea correcto
        )

    def setUp(self):
        # Configuramos el tablero y las piezas necesarias para los tests
        self.tablero = Tablero()
        self.rey_blanco = Rey("blanco", self.tablero)
        self.rey_negro = Rey("negro", self.tablero)
        self.peon_blanco = Peon("blanco", self.tablero)
        self.peon_negro = Peon("negro", self.tablero)

    # Test para verificar que el rey puede moverse libremente dentro de su rango permitido
    def test_movimiento_libre(self):
        # Colocamos al rey en el centro del tablero
        self.tablero.poner_pieza(4, 4, self.rey_blanco)
        posiciones = self.rey_blanco.obtener_posiciones_mover(4, 4)

        # Las posiciones esperadas son las adyacentes a (4,4)
        esperados = [
            (3, 4), (5, 4), (4, 3), (4, 5), 
            (3, 3), (3, 5), (5, 3), (5, 5)
        ]
        self.assertCountEqual(posiciones, esperados)

    # Test para verificar que el rey no pueda moverse a una casilla ocupada por una pieza aliada
    def test_movimiento_bloqueado_por_pieza_propia(self):
        # Colocamos al rey y un peón blanco en una casilla adyacente
        self.tablero.poner_pieza(4, 4, self.rey_blanco)
        self.tablero.poner_pieza(3, 4, self.peon_blanco)  # El peón bloquea el movimiento

        posiciones = self.rey_blanco.obtener_posiciones_mover(4, 4)

        # Las posiciones esperadas excluyen (3,4), ya que está ocupada por el peón aliado
        esperados = [
            (5, 4), (4, 3), (4, 5), 
            (3, 3), (3, 5), (5, 3), (5, 5)
        ]
        self.assertCountEqual(posiciones, esperados)

    # Test para verificar que el rey puede capturar una pieza enemiga
    def test_movimiento_con_captura(self):
        # Colocamos al rey y un peón negro en una casilla adyacente
        self.tablero.poner_pieza(4, 4, self.rey_blanco)
        self.tablero.poner_pieza(3, 4, self.peon_negro)  # Peón enemigo en (3,4)

        posiciones = self.rey_blanco.obtener_posiciones_mover(4, 4)

        # El rey debe poder moverse a (3,4) para capturar el peón enemigo
        esperados = [
            (3, 4), (5, 4), (4, 3), (4, 5), 
            (3, 3), (3, 5), (5, 3), (5, 5)
        ]
        self.assertCountEqual(posiciones, esperados)

    # Test para verificar que el rey se restringe cuando está cerca del borde del tablero
    def test_movimiento_fuera_del_tablero(self):
        # Colocamos al rey en la esquina superior izquierda del tablero
        self.tablero.poner_pieza(0, 0, self.rey_blanco)
        posiciones = self.rey_blanco.obtener_posiciones_mover(0, 0)

        # Los movimientos permitidos desde la esquina superior izquierda
        esperados = [(0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(posiciones, esperados)


if __name__ == '__main__':
    unittest.main()
