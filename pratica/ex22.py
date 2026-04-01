# Faça um programa que leia três números e mostre-os em ordem decrescente:

num1 = int(input("num1: "))

num2 = int(input("num2: "))

num3 = int(input("num3: "))

if num1 >= num2 and num1 >= num3:
    primeiro = num1
    if num2 >= num3:
        segundo, terceiro = num2, num3
    else:
        segundo, terceiro = num3, num2
elif num2 >= num1 and num2 >= num3:
    primeiro = num2
    if num1 >= num3:
        segundo, terceiro = num1, num3
    else:
        segundo, terceiro = num3, num1
else:
    primeiro = num3
    if num1 >= num2:
        segundo, terceiro = num1, num2
    else:
        segundo, terceiro = num2, num1

print(f'A ordem decrescente é: {primeiro}, {segundo}, {terceiro}')