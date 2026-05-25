caminho_arq = '/home/gabriel/Área de trabalho/Udemy/aula69.txt'


# arquivo = open(caminho_arq, 'w')

# arquivo.close()

with open(caminho_arq, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Ola mundo\n')
    arquivo.write('arquivo vai ser fechado')

print('O código rodou e o arquivo foi fechado com sucesso.')