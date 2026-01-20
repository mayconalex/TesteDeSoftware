import unittest
from legado import calcular


class TestLegado(unittest.TestCase):
    def test_calcular_sem_desconto(self):
        self.assertEqual(calcular(1, 100), 100)

    def test_calcular_desconto_10(self):
        self.assertEqual(calcular(2, 100), 100)
        self.assertEqual(calcular(2, 101), 90.9)

    def test_calcular_desconto_20(self):
        self.assertEqual(calcular(3, 100), 80)

    def test_calcular_tipo_invalido(self):
        self.assertEqual(calcular(4, 100), 100)


if __name__ == "__main__":
    unittest.main()
