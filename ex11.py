# Minha Tentativa:

# def par():
#     while True:
#         num = int(input("Digite um numero: "))
#         if num % 2 == 0:
#             print("É par")
#         else:
#             print("É impar")
#         break
# par()

def par(num):
    return "par" if num % 2 == 0 else "impar"
numero = int(input("Digite um numero: "))
resultado = par(numero)
print(f"O número é {resultado}")

