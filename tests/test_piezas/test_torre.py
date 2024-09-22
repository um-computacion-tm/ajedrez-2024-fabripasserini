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

   # def test_mover_vertical_desc(self):
   #     tablero = Tablero()
   #     torre = Torre("BLANCO", tablero)
   #     posibles = torre.posibles_posiciones_vd(4, 1)
   #     self.assertEqual(
   #         posibles,
   #         [(5, 1), (6, 1), (7, 1)]
   #     )
    
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
   
        
if __name__ == '__main__':
    unittest.main()