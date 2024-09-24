import unittest
from chess.piezas.torre import Torre
from chess.tablero import Tablero
from chess.piezas.peon import Peon

class TestTorre(unittest.TestCase):


    def test_str(self):
        tablero = Tablero()
        torre = Torre("BLANCO", tablero)
        self.assertEqual(
            str(torre),
            "♜",
        )

    def test_mover_vertical_asc(self):
        tablero = Tablero()
        torre = Torre("BLANCO", tablero)
        posibles = torre.posibles_posiciones_va(4, 1)
        self.assertEqual(
            posibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )
    
    def test_mover_vertical_desc_con_pieza_propia(self):
        tablero = Tablero()
        tablero.poner_pieza(6, 1, Peon("BLANCO", tablero))
        torre = Torre("BLANCO", tablero)
        tablero.poner_pieza(4, 1, torre)
        posibles = torre.posibles_posiciones_vd(4, 1)
        self.assertEqual(
            posibles,
            [(5, 1)]
        )
    def test_mover_vertical_desc_con_pieza_contraria(self):
        tablero = Tablero()
        tablero.poner_pieza(6, 1, Peon("NEGRO", tablero))
        torre = Torre("BLANCO", tablero)
        tablero.poner_pieza(4, 1, torre)
        posibles = torre.posibles_posiciones_vd(4, 1)
        self.assertEqual(
            posibles,
            [(5, 1), (6, 1)]
        )

    def test_mover_diagonal_desc(self):
        tablero = Tablero()
        torre = tablero.obtener_pieza(columna=0, fila=0)
        es_posible = torre.posiciones_validas(
            desde_fila=0,
            desde_columna=0,
            hasta_fila=1,
            hasta_columna=1,
        )
        self.assertFalse(es_posible)

    def setUp(self):
        self.tablero = Tablero()
        self.torre_blanca = Torre('BLANCO', self.tablero)
        self.torre_negra = Torre('NEGRO', self.tablero)
        self.tablero.poner_pieza(3, 3, self.torre_blanca)  
    
    def test_posibles_posiciones_hd_sin_obstaculos(self):
        resultado = self.torre_blanca.posibles_posiciones_hd(3, 3)
        esperado = [(3, 4), (3, 5), (3, 6), (3, 7)]  
        self.assertEqual(resultado, esperado)

    def test_posibles_posiciones_hd_con_obstaculo(self):
        self.tablero.poner_pieza(3, 5, self.torre_negra)  
        resultado = self.torre_blanca.posibles_posiciones_hd(3, 3)
        esperado = [(3, 4), (3, 5)] 
        self.assertEqual(resultado, esperado)

    def test_posibles_posiciones_hd_con_aliado(self):
        self.tablero.poner_pieza(3, 5, Torre('BLANCO', self.tablero))  
        resultado = self.torre_blanca.posibles_posiciones_hd(3, 3)
        esperado = [(3, 4)]  
        self.assertEqual(resultado, esperado)

    def test_posibles_posiciones_hi_sin_obstaculos(self):
        resultado = self.torre_blanca.posibles_posiciones_hi(3, 3)
        esperado = [(3, 2), (3, 1), (3, 0)]  
        self.assertEqual(resultado, esperado)

    def test_posibles_posiciones_hi_con_obstaculo(self):
        self.tablero.poner_pieza(3, 1, self.torre_negra) 
        resultado = self.torre_blanca.posibles_posiciones_hi(3, 3)
        esperado = [(3, 2), (3, 1)] 
        self.assertEqual(resultado, esperado)

    def test_posibles_posiciones_hi_con_aliado(self):
        self.tablero.poner_pieza(3, 1, Torre('BLANCO', self.tablero))  
        resultado = self.torre_blanca.posibles_posiciones_hi(3, 3)
        esperado = [(3, 2)]  
        self.assertEqual(resultado, esperado)

   
        
if __name__ == '__main__':
    unittest.main()