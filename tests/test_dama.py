import unittest
from chess.piezas.dama import Dama
from chess.tablero import Tablero
from chess.piezas.pieza import Pieza

class TestDama(unittest.TestCase):
    # Comprobamos que funcione el método str para la representación de la dama
    def test_str(self):
        # Creamos un tablero y una dama blanca
        tablero = Tablero()
        peon = Dama("BLANCO", tablero)
        
        # Verificamos que la representación en cadena de la dama es la esperada
        self.assertEqual(
            str(peon),
            "♛",
        )

    # Configuración previa a cada test
    def setUp(self):
        # Inicializamos un tablero y colocamos una dama blanca y una negra
        self.tablero = Tablero()
        self.dama_blanca = Dama("blanco", self.tablero)
        self.dama_negra = Dama("negro", self.tablero)
    
    # Test para verificar los movimientos válidos de la dama sin obstrucciones
    def test_movimiento_libre(self):
        # Colocamos la dama blanca en el centro del tablero
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        
        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # Movimientos válidos esperados (diagonales, verticales y horizontales)
        esperados = [
            (3, 3), (2, 2), (1, 1), (3, 5), (2, 6), (1, 7),  # Diagonales
            (5, 5), (5, 3), (6, 2),           # Diagonales
            (5, 4), (6, 4),  (3, 4), (2, 4), (1, 4),  # Verticales
            (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)   # Horizontales
        ]
        
        # Verificamos que todas las posiciones esperadas están en los movimientos posibles
        for posicion in esperados:
            self.assertIn(posicion, posiciones)

    # Test para verificar que la dama no puede moverse a una casilla ocupada por una pieza amiga
    def test_movimiento_bloqueado_por_pieza_misma(self):
        # Colocamos la dama blanca en el centro y una pieza aliada en su camino
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        self.tablero.poner_pieza(6, 4, self.dama_blanca)  # Bloquea movimiento vertical hacia abajo
        
        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # Verificamos que la dama no puede moverse a (6, 4) porque está bloqueada por la pieza amiga
        self.assertNotIn((6, 4), posiciones)

    # Test para verificar que la dama puede capturar una pieza enemiga
    def test_movimiento_con_captura(self):
        # Colocamos la dama blanca en el centro y una pieza enemiga en su camino
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        self.tablero.poner_pieza(6, 4, self.dama_negra)  # Pieza enemiga para capturar
        
        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # Verificamos que la dama puede capturar la pieza enemiga en (6, 4)
        self.assertIn((6, 4), posiciones)

    # Test para verificar que la dama no puede moverse más allá de una pieza bloqueante
    def test_movimiento_bloqueado_por_piezas(self):
        # Colocamos la dama blanca en el centro y una pieza enemiga en la diagonal
        self.tablero.poner_pieza(4, 4, self.dama_blanca)
        self.tablero.poner_pieza(6, 6, self.dama_negra)  # Pieza enemiga en la diagonal
        
        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.dama_blanca.obtener_posiciones_mover(4, 4)
        
        # Verificamos que la dama puede moverse hasta (6, 6) pero no más allá
        self.assertIn((6, 6), posiciones)
        self.assertNotIn((7, 7), posiciones)

    # Test para verificar los movimientos horizontales de la dama
    def test_obtener_posiciones_horizontales(self):
        # Colocamos la dama blanca en el tablero
        self.tablero.poner_pieza(2, 2, self.dama_blanca)

        # Colocamos una pieza aliada a la izquierda
        pieza_aliada = Pieza("blanco", self.tablero)
        self.tablero.poner_pieza(2, 1, pieza_aliada)

        # Colocamos una pieza enemiga a la derecha
        pieza_enemiga = Pieza("negro", self.tablero)
        self.tablero.poner_pieza(2, 3, pieza_enemiga)

        # Obtenemos las posiciones que la dama puede mover
        posiciones = self.dama_blanca.obtener_posiciones_horizontales(2, 2)

        # Verificamos que la dama no puede moverse a la izquierda debido a la pieza aliada
        self.assertNotIn((2, 1), posiciones)  # Bloqueado por pieza aliada

        # Verificamos que la dama puede moverse a la derecha hasta la pieza enemiga
        self.assertIn((2, 3), posiciones)  # Captura la pieza enemiga

        # Verificamos que la dama no puede moverse más allá de la pieza enemiga
        self.assertNotIn((2, 4), posiciones)  # Bloqueado por la pieza enemiga

if __name__ == '__main__':
    unittest.main()
