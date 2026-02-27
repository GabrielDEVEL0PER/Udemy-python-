import sys

iterable = ['Eu', 'Tenho', '__iter__']

interator = iter(iterable)
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)