import unittest
from chess.piezas.caballo import Caballo
from chess.tablero import Tablero

class TestCaballo(unittest.TestCase):

    # Comprobamos que funcione el método str para la representación del caballo
    def test_str(self):
        # Creamos un tablero y un caballo blanco
        tablero = Tablero()
        caballo = Caballo("BLANCO", tablero)
        
        # Verificamos que la representación en cadena del caballo es la esperada
        self.assertEqual(
            str(caballo),
            "♞",
        )

    # Configuración previa a cada test
    def setUp(self):
        # Creamos un tablero vacío y dos caballos, uno blanco y uno negro
        self.tablero = Tablero()
        self.caballo_blanco = Caballo("BLANCO", self.tablero)
        self.caballo_negro = Caballo("NEGRO", self.tablero)
    
    # Test para verificar los movimientos válidos del caballo sin obstrucciones
    def test_movimiento_libre(self):
        # Colocamos el caballo en la posición (4, 4)
        self.tablero.poner_pieza(4, 4, self.caballo_blanco)
        
        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.caballo_blanco.obtener_posiciones_mover(4, 4)

        # Movimientos esperados del caballo desde (4, 4)
        esperados = [ (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
        
        # Verificamos que todas las posiciones esperadas están en los movimientos posibles
        for posicion in esperados:
            self.assertIn(posicion, posiciones)
    
    # Test para verificar que el caballo no puede moverse a una casilla ocupada por una pieza amiga
    def test_movimiento_bloqueado_por_pieza_misma(self):
        # Colocamos el caballo blanco en (4, 4)
        self.tablero.poner_pieza(4, 4, self.caballo_blanco)
        
        # Colocamos otra pieza amiga (caballo blanco) en (6, 5)
        pieza_amiga = Caballo("BLANCO", self.tablero)
        self.tablero.poner_pieza(6, 5, pieza_amiga)

        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.caballo_blanco.obtener_posiciones_mover(4, 4)
        
        # Verificamos que el caballo no puede moverse a (6, 5) porque está bloqueado por la pieza amiga
        self.assertNotIn((6, 5), posiciones)
    
    # Test para verificar que el caballo puede capturar una pieza enemiga
    def test_movimiento_con_captura(self):
        # Colocamos el caballo blanco en (4, 4)
        self.tablero.poner_pieza(4, 4, self.caballo_blanco)
        
        # Colocamos una pieza enemiga (caballo negro) en (6, 5)
        pieza_enemiga = Caballo("NEGRO", self.tablero)
        self.tablero.poner_pieza(6, 5, pieza_enemiga)

        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.caballo_blanco.obtener_posiciones_mover(4, 4)

        # Verificamos que el caballo puede capturar la pieza enemiga en (6, 5)
        self.assertIn((6, 5), posiciones)

    # Test para verificar que el caballo no puede moverse fuera del tablero
    def test_movimiento_fuera_del_tablero(self):
        # Colocamos el caballo blanco en (1, 1), cerca del borde del tablero
        self.tablero.poner_pieza(1, 1, self.caballo_blanco)
        
        # Obtenemos las posiciones válidas de movimiento
        posiciones = self.caballo_blanco.obtener_posiciones_mover(1, 1)

        # Movimientos esperados desde la posición (1, 1)
        esperados = [(0, 3), (3, 0), (3, 2), (2, 3)]
        
        # Verificamos que los movimientos esperados están en las posiciones válidas
        for posicion in esperados:
            self.assertIn(posicion, posiciones)
        
        # Movimientos no válidos fuera del tablero
        no_validos = [(0, 2), (1, 3), (-1, 2)]
        
        # Verificamos que los movimientos fuera del tablero no son válidos
        for posicion in no_validos:
            self.assertNotIn(posicion, posiciones)

if __name__ == '__main__':
    unittest.main()
