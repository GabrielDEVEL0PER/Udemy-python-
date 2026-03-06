import math
area_pintada = float(input('Digite os m² da área: '))

litros_necessarios = area_pintada / 6

latas1 = math.ceil(litros_necessarios / 18)

preco_total1 = latas1 * 80

latas2 = math.ceil(litros_necessarios / 3.6 )

preco_total2 = latas2 * 25

print(f'Se você comprar em latas de 18 litros o preço é esse {preco_total1}')
print(f'Se você comprar em latas de 3.6 litros o preço é esse {preco_total2}')