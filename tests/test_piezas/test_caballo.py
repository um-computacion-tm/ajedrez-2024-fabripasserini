import unittest
from chess.piezas.caballo import Caballo
from chess.tablero import Tablero

class TestCaballo(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        caballo = Caballo("BLANCO", tablero)
        self.assertEqual(
            str(caballo),
            "♞",
        )

    def setUp(self):
        self.tablero = Tablero()
        self.caballo_blanco = Caballo("BLANCO", self.tablero)
        self.caballo_negro = Caballo("NEGRO", self.tablero)
    
    def test_movimiento_libre(self):
        self.tablero.poner_pieza(4, 4, self.caballo_blanco)
        posiciones = self.caballo_blanco.obtener_posiciones_mover(4, 4)

    
        esperados = [ (2, 5), (2, 3), (5, 6), (5, 2), (3, 6), (3, 2)]
        for posicion in esperados:
            self.assertIn(posicion, posiciones)
    
    def test_movimiento_bloqueado_por_pieza_misma(self):
        self.tablero.poner_pieza(4, 4, self.caballo_blanco)
        pieza_amiga = Caballo("BLANCO", self.tablero)
        self.tablero.poner_pieza(6, 5, pieza_amiga)

        posiciones = self.caballo_blanco.obtener_posiciones_mover(4, 4)
        
        self.assertNotIn((6, 5), posiciones)
    
    def test_movimiento_con_captura(self):
        self.tablero.poner_pieza(4, 4, self.caballo_blanco)
        pieza_enemiga = Caballo("NEGRO", self.tablero)
        self.tablero.poner_pieza(6, 5, pieza_enemiga)

        posiciones = self.caballo_blanco.obtener_posiciones_mover(4, 4)

        self.assertIn((6, 5), posiciones)

    def test_movimiento_fuera_del_tablero(self):
        self.tablero.poner_pieza(1, 1, self.caballo_blanco)
        posiciones = self.caballo_blanco.obtener_posiciones_mover(1, 1)

        esperados = [(0, 3),(3, 0), (3, 2), (2, 3)]
        for posicion in esperados:
            self.assertIn(posicion, posiciones)
        
       
        no_validos = [(0, 2), (1, 3),(-1, 2)]
        for posicion in no_validos:
            self.assertNotIn(posicion, posiciones)

if __name__ == '__main__':
    unittest.main()