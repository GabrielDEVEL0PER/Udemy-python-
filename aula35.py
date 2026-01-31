pessoa = {
    'nome': 'Gabriel Aguiar',
    'sobrenome': 'Cordeiro', 
    'idade': 24,
    'altura': 1.83,
    'endereços': [
          {'rua': 'tal tal', 'número': 123},
          {'rua': 'outra rua', 'número': 123},
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()


for chave in pessoa:
    print(chave, pessoa[chave])