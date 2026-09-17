from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self._nome = None
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    @abstractmethod
    def nome(self,nome):
        ...

class Cachorro(Animal):
    @Animal.nome.setter
    def nome(self, nome):
        if not nome:
            raise ValueError("Cachorro precisa de um nome!!")
        self._nome = nome.upper()

class Gato(Animal):
    @Animal.nome.setter
    def nome(self, nome):
        self._nome = nome.lower()

class Passaro(Animal):
    @Animal.nome.setter
    def nome(self, nome):
        self._nome = nome.lower()

cachorro = Cachorro("REX")
gato = Gato("Miau")
passaro = Passaro("Piau")
print(cachorro.nome)
print(gato.nome)
print(passaro.nome)
