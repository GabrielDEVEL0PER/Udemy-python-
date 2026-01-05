nome = input('Qual seu nome?: ')

cont_nome = len(nome)

i = 0

while i < cont_nome:
    print(nome[i], end='$')
    i += 1