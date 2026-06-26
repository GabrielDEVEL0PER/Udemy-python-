import json 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Gabriel', 20)
p2 = Pessoa ('Ana', 25)


dados = [
    {'nome': p1.nome, 'idade': p1.idade},
    {'nome': p2.nome, 'idade': p2.idade}
]

with open('pessoas.json', 'w',) as arquivo:
    json.dump(dados, arquivo)

print('Dados Salvos')

