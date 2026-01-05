# repitor = 0 

# lista = ['Maria', 'Helena', 'Luiz', 'Gabriel']

# for nome in lista:

#     repitor += 1
#     print(nome, repitor)

lista = ['Maria', 'Helena', 'Luiza']

lista.append('João')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
