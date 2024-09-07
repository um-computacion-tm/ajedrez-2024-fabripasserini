import unittest
from chess.excepciones import movimiento_inválido, movimiento_sin_pieza, turno_invalido, fuera_del_tablero

class TestExcepcionesAjedrez(unittest.TestCase):

    def test_movimiento_invalido(self):
        with self.assertRaises(movimiento_inválido) as contexto:
            raise movimiento_inválido()
        self.assertEqual(str(contexto.exception.mensaje), "El movimiento no es válido")

    def test_movimiento_sin_pieza(self):
        with self.assertRaises(movimiento_sin_pieza) as contexto:
            raise movimiento_sin_pieza()
        self.assertEqual(str(contexto.exception.mensaje), "La posicion se encuentra vacía")

    def test_turno_invalido(self):
        with self.assertRaises(turno_invalido) as contexto:
            raise turno_invalido()
        self.assertEqual(str(contexto.exception.mensaje), "El turno no es válido")

    def test_fuera_del_tablero(self):
        with self.assertRaises(fuera_del_tablero) as contexto:
            raise fuera_del_tablero()
        self.assertEqual(str(contexto.exception.mensaje), "La posicion indicada se encuentra fuera del tablero")

if __name__ == '__main__':
    unittest.main()
