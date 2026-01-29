nume = int(input("Digite um numero: "))

opção = input("Duplicar, Triplicar,Quadruplicar: ").lower()


def dupli(n):
    return n * 2
def tri(n):
    return n * 3
def quad(n):
    return n * 4

if opção == 'dupli':
    print(dupli(nume))
elif opção == 'tri':
    print(tri(nume))
elif opção == 'quad':
    print(quad(nume))
else:
    print("Opção invalida")


     

