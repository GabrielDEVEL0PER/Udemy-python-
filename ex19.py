from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

class Conta(ABC):
    def __init__(self, numero, saldo, agencia):
        self._numero = numero
        self._saldo = saldo
        self._agencia = agencia
    @abstractmethod
    def sacar(self, valor):
        ...
    def depositar(self, valor):
        self._saldo += valor

class ContaCorrente(Conta):
        def __init__(self, numero, saldo, agencia, limite):
            super().__init__(numero, saldo, agencia)
            self._limite = limite
        
        def sacar(self, valor):
            if valor <= self._saldo + self._limite:
                self._saldo -= valor
            else: 
                print('Saldo insuficiente')




class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
        else:
            print('Saldo insuficiente')


class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []


conta1 = ContaCorrente(1, 100, '0001', 50)
cliente1 = Cliente('Ana', 30, conta1)

banco = Banco()
banco.clientes.append(cliente1)
banco.contas.append(conta1)


conta1 = ContaCorrente(1, 100, '0001', 50)

print(conta1._saldo)  
conta1.sacar(120)
print(conta1._saldo)   
print(conta1._saldo)   