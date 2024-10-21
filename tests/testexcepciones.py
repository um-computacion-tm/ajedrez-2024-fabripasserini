import unittest
from chess.excepciones import movimiento_inválido, turno_invalido, fuera_del_tablero, movimiento_sin_pieza

class TestExcepcionesAjedrez(unittest.TestCase):

    def test_movimiento_invalido(self):
        with self.assertRaises(movimiento_inválido) as context:
            raise movimiento_inválido()
        self.assertEqual(str(context.exception), "El movimiento no es válido")

        # Test con mensaje personalizado
        with self.assertRaises(movimiento_inválido) as context:
            raise movimiento_inválido("Movimiento no permitido")
        self.assertEqual(str(context.exception), "Movimiento no permitido")

    def test_turno_invalido(self):
        with self.assertRaises(turno_invalido) as context:
            raise turno_invalido()
        self.assertEqual(str(context.exception), "El turno no es válido")

        # Test con mensaje personalizado
        with self.assertRaises(turno_invalido) as context:
            raise turno_invalido("No es tu turno")
        self.assertEqual(str(context.exception), "No es tu turno")

    def test_fuera_del_tablero(self):
        with self.assertRaises(fuera_del_tablero) as context:
            raise fuera_del_tablero()
        self.assertEqual(str(context.exception), "La posición indicada se encuentra fuera del tablero")

        # Test con mensaje personalizado
        with self.assertRaises(fuera_del_tablero) as context:
            raise fuera_del_tablero("Posición fuera del rango")
        self.assertEqual(str(context.exception), "Posición fuera del rango")

    def test_movimiento_sin_pieza(self):
        with self.assertRaises(movimiento_sin_pieza) as context:
            raise movimiento_sin_pieza()
        self.assertEqual(str(context.exception), "Movimiento sin pieza")

        # Test con mensaje personalizado
        with self.assertRaises(movimiento_sin_pieza) as context:
            raise movimiento_sin_pieza("No hay ninguna pieza en la posición seleccionada")
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición seleccionada")

if __name__ == "__main__":
    unittest.main()

