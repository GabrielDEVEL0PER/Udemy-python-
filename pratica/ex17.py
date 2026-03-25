letra = input("Digite uma letra: ")

if letra.isalpha() and len(letra) == 1:
    if letra.lower() in 'aeiou':
        print('É vogal')
    else:
        print('É consoante')
else:
    ("Erro: você não digitou uma letra válida")