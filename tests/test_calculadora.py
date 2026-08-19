import unittest
from app.calculadora import sumar, restar


class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
