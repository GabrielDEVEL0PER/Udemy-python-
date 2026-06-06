import json 

# pessoa = {
#     'nome': 'Gabriel Aguiar',
#     'sobrenome': 'Aguiar',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 42},
#         {'rua': 'R2', 'numero': 55},

#     ],
#     'altura': 1.83,
#     'numeros_preferidos': (2,4,6,8,10),
#     'dev': True,
#     'nada': None,

# }

# with open('aula70.json', 'w') as arquivo: 
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#     )

with open ('aula70.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])