import unittest
from chess.piezas.dama import Dama
from chess.tablero import Tablero

class TestDama(unittest.TestCase):
    def test_str(self):
        tablero = Tablero()
        peon = Dama("BLANCO", tablero)
        self.assertEqual(
            str(peon),
            "♛",
        )

    def setUp(self):
        # Inicializamos un tablero y colocamos una dama en él
        self.tablero = Tablero()
        self.dama_blanca = Dama("blanco", self.tablero)
        self.dama_negra = Dama("negro", self.tablero)
    
    def test_movimiento_libre(self):
        
        # Colocamos la dama blanca en el centro del tablero
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        
        # Obtenemos las posibles posiciones a las que puede moverse
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # Movimientos válidos esperados (diagonales, verticales y horizontales)
        esperados = [
            (3, 3), (2, 2), (1, 1), (3, 5), (2, 6), (1, 7),  # Diagonales
            (5, 5), (5, 3), (6, 2),           # Diagonales
            (5, 4), (6, 4),  (3, 4), (2, 4), (1, 4),  # Verticales
            (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)   # Horizontales
        ]
        
        for posicion in esperados:
            self.assertIn(posicion, posiciones)

    def test_movimiento_bloqueado_por_pieza_misma(self):
        
        # Colocamos la dama blanca en el centro y una pieza aliada en su camino
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        self.tablero.poner_pieza(6, 4, self.dama_blanca)  # Bloquea movimiento vertical hacia abajo
        
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # La posición (6, 4) debe estar bloqueada por la pieza aliada
        self.assertNotIn((6, 4), posiciones)

    def test_movimiento_con_captura(self):
        
        # Colocamos la dama blanca en el centro y una pieza enemiga en su camino
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        self.tablero.poner_pieza(6, 4, self.dama_negra)  # Pieza enemiga para capturar
        
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # La dama debe poder capturar en (6, 4)
        self.assertIn((6, 4), posiciones)



    def test_movimiento_bloqueado_por_piezas(self):
       
        # Colocamos la dama blanca y una pieza enemiga en el tablero
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        self.tablero.poner_pieza(6, 6, self.dama_negra)  # Pieza enemiga en la diagonal
        
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # La dama debe poder moverse hasta (6, 6) y no más allá
        self.assertIn((6, 6), posiciones)
        self.assertNotIn((7, 7), posiciones)


if __name__ == '__main__':
    unittest.main()


