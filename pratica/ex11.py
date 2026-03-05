import math

area_pintada = float(input("Digite a área pintada em m²: "))

litros_necessarios = area_pintada / 3

latas = math.ceil(litros_necessarios / 18)

preco_total = latas * 80

print(f'Quantidade de latas: {latas}')
print(f'Preço total: {preco_total:.2f}')


