import unittest
from chess.piezas.rey import Rey
from chess.piezas.peon import Peon
from chess.tablero import Tablero

class TestRey(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        rey = Rey("BLANCO", tablero)
        self.assertEqual(
            str(rey),
            "♚",
        )
    
    def setUp(self):
        self.tablero = Tablero()
        self.rey_blanco = Rey("blanco", self.tablero)
        self.rey_negro = Rey("negro", self.tablero)
        self.peon_blanco = Peon("blanco", self.tablero)
        self.peon_negro = Peon("negro", self.tablero)

    def test_movimiento_libre(self):
        # Colocar el rey en el centro del tablero
        self.tablero.poner_pieza(4, 4, self.rey_blanco)
        posiciones = self.rey_blanco.obtener_posiciones_mover(4, 4)

        # Movimientos posibles desde el centro del tablero (4,4)
        esperados = [
            (3, 4), (5, 4), (4, 3), (4, 5), 
            (3, 3), (3, 5), (5, 3), (5, 5)
        ]
        self.assertCountEqual(posiciones, esperados)

    def test_movimiento_bloqueado_por_pieza_propia(self):
        # Colocar el rey en el centro y un peón blanco en una casilla adyacente
        self.tablero.poner_pieza(4, 4, self.rey_blanco)
        self.tablero.poner_pieza(3, 4, self.peon_blanco)  # Peón aliado arriba del rey

        posiciones = self.rey_blanco.obtener_posiciones_mover(4, 4)

        # Movimientos posibles (excluyendo la casilla bloqueada por el peón aliado)
        esperados = [
            (5, 4), (4, 3), (4, 5), 
            (3, 3), (3, 5), (5, 3), (5, 5)
        ]
        self.assertCountEqual(posiciones, esperados)

    def test_movimiento_con_captura(self):
        # Colocar el rey en el centro y un peón negro en una casilla adyacente
        self.tablero.poner_pieza(4, 4, self.rey_blanco)
        self.tablero.poner_pieza(3, 4, self.peon_negro)  # Peón enemigo arriba del rey

        posiciones = self.rey_blanco.obtener_posiciones_mover(4, 4)

        # Movimientos posibles (incluyendo la casilla donde está el peón enemigo)
        esperados = [
            (3, 4), (5, 4), (4, 3), (4, 5), 
            (3, 3), (3, 5), (5, 3), (5, 5)
        ]
        self.assertCountEqual(posiciones, esperados)

    def test_movimiento_fuera_del_tablero(self):
        # Colocar el rey cerca del borde del tablero
        self.tablero.poner_pieza(0, 0, self.rey_blanco)
        posiciones = self.rey_blanco.obtener_posiciones_mover(0, 0)

        # Movimientos posibles desde la esquina superior izquierda
        esperados = [(0, 1), (1, 0), (1, 1)]
        self.assertCountEqual(posiciones, esperados)


if __name__ == '__main__':
    unittest.main()