import unittest
from chess.main import Ajedrez

class TestAjedrez(unittest.TestCase):

    def setUp(self):
        self.ajedrez = Ajedrez()

    def test_mover_posiciones_invalidas(self):
        with self.assertRaises(ValueError):
            self.ajedrez.mover(-1, 0, 0, 0)
        with self.assertRaises(ValueError):
            self.ajedrez.mover(0, 0, 8, 0)


if __name__ == "__main__":
    unittest.main()
