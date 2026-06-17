class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Gabriel', 'Aguiar')

p2 = Pessoa('Maria', 'Joana')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)

print(p2.sobrenome)