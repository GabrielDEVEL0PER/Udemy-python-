# # s1 = set() vazio
# # s1 = {'Luiz', 1, 2, 3} com dados
# # print(s1)
# # l1 = [1, 2, 2, 2, 3 , 3, 3, 3, 1]
# # s1 = set(l1)
# # l2 = list(s1)
# # print(l2)
# # s1 = {'Luiz', 1, 2, 3}

# s1 = set()
# s1.add('Luiz')
# s1.add(1)
# s1.update(('Olá Mundo', 1, 2, 3))
# # s1.clear()
# s1.discard('Olá Mundo')
# # print(s1)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s2 - s1
# print(s3)

letras = set()

while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)