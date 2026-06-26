import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

with open('pessoas.json', 'r') as arquivo:
    dados = json.load(arquivo)

pessoas = [Pessoa(d['nome'], d['idade']) for d in dados]

for p in pessoas:
    print(f'{p.nome} tem {p.idade} anos')