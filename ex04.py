numero = input("Digite um numero inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero %2 == 0:
        print('Seu numero é par')
    
    else:
        print("Seu numero é impar")
else:
    print("Digite apenas numeros inteiros!!!")

