nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media == 10:
    print(f'{media} Aprovado com distinção')

elif media >= 7:
    print(f'{media} Aprovado')
elif media < 7:
    print(f'{media} Reprovado')
else:
    print('Erro')