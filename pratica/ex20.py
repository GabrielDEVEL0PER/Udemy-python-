import math

num1 = int(input("NUM1: "))
num2 = int(input("NUM2: "))
num3 = int(input("NUM3: "))

if num1 >= num2 and num1 >= num3:
    print(f'Maior foi {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'Maior foi {num2}')
else:
    print(f'Maior foi {num3}')

# maior = max(num1, num2, num3)

# menor = min(num1, num2, num3)

# print(f'Maior foi{maior}')

# print(f'Menor foi {menor}')

if num1 <= num2 and num1 <= num3:
    print(f'Maior foi: {num1}')
elif num2 <= num1 and num2 <= num3:
    print(f'Maior foi: {num2}')
else:
    print(f'Menor foi: {num3}')