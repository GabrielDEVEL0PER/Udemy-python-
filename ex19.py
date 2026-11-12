from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

class Clinte(Pessoa):
    Conta = 1

class Conta(ABC):
    def agencia(self, numero, saldo):
        self._numero = numero
        self._idade = saldo
    @abstractmethod
    def sacar(self, valor):
        self._valor = valor

class ContaCorrente(Conta):
    def sacar(self, valor):
        self._valor = valor

class ContaPoupanca(Conta):
    def sacar(self, valor):
        self._valor = valor

class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

banco = Banco()
banco.clientes.append(Clinte)
banco.contas.append(Conta)