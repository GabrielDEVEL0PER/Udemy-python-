def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))

    resultado = []

    for i in range(intervalo):
        resultado.append((lista1[i], lista2[i]))
    return resultado

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']


print(zipper(cidades, estados))