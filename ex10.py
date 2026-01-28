def multi (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros = 1, 2, 10, 20
outra_soma = multi(*numeros)
print(outra_soma)

