import math

while True:
    try:
        primeiro_numero = int(input("primeiro numero: "))
        segundo_numero = int(input(" segundo numero: "))
        break
    except ValueError:
        print("Só pode digitar numeros!!!")

maior = max (primeiro_numero, segundo_numero)
minimo = min (primeiro_numero, segundo_numero)

print(f"O maior número é {maior} e o menor é {minimo}")
