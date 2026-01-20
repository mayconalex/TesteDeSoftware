Feature: Gerenciamento de Conta
    Scenario: Saque com saldo suficiente
        Given a conta tem saldo inicial de 100
        When o usuário saca 30
        Then o saldo final deve ser 70