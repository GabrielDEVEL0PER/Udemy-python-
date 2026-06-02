


caminho_arq = '/home/gabriel/Área de trabalho/Udemy/aula69.txt'


# arquivo = open(caminho_arq, 'w')

# arquivo.close()

# with open(caminho_arq, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(

#         ("Linha 3\n", 'Linha4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())

#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
# print('#' * 10)

# with open(caminho_arq, 'r') as arquivo: 
#     print(arquivo.read())



with open(caminho_arq, 'w') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(

        ("Linha 3\n", 'Linha4\n')
    )