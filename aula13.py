numero = input('Digite um numero: ')

try:
    numero_float = float(numero)
    print('FLOAT', numero_float)
    print(f'o dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')