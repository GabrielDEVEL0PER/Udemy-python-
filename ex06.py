nome = input("Digite seu primeiro nome: ")

contador = len(nome)
if contador <= 4:
    print("Seu nome é curto")
elif 5 <= contador <= 6:
    print("Seu nome é medio")
else:
    print('Seu nome é grande ')

print(contador)