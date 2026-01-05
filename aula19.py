texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')

senha_salva = '123456'

senha_digitada = ''

repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x):')

    repeticoes += 1

print(repeticoes)

numeros = range (0, 100, 8)

for numero in numeros:
    print(numero)