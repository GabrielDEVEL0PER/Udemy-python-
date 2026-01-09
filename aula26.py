string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [

    ['Maria', 'Helena'],

    ['Elaine', ],

    ['Luiz', 'João', 'Eduarda'],

]

# a,b, *_, ap, u = lista
# print(a, u, ap)

# print(*tupla)
print(*salas, sep='\n')