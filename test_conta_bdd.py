import pytest
from pytest_bdd import scenario, given, when, then, parsers
from conta import ContaBancaria


@scenario("conta.feature", "Saque com saldo suficiente")
def test_saque_sucesso():
    pass


@pytest.fixture
def conta():
    return ContaBancaria()


@given(parsers.parse("a conta tem saldo inicial de {valor:d}"))
def saldo_inicial(conta, valor):
    conta.depositar(valor)


@when(parsers.parse("o usuário saca {valor:d}"))
def acao_sacar(conta, valor):
    conta.sacar(valor)


@then(parsers.parse("o saldo final deve ser {valor:d}"))
def verificar_saldo(conta, valor):
    assert conta.saldo == valor
