import unittest
from conta import ContaBancaria


class TestContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria()

    def test_saldo_zero(self):
        self.assertEqual(0, self.conta.saldo)

    def test_saldo_aumenta(self):
        self.conta.depositar(100)
        self.assertEqual(100, self.conta.saldo)

    def test_saldo_saque(self):
        self.conta.depositar(100)
        self.conta.sacar(40)
        self.assertEqual(60, self.conta.saldo)

    def test_saldo_insuficiente_saque(self):
        self.conta.depositar(20)
        resultado = self.conta.sacar(25)
        self.assertFalse(resultado)
        self.assertEqual(20, self.conta.saldo)


if __name__ == "__main__":
    unittest.main()
