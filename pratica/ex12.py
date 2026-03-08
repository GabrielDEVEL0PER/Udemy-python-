import math
area_pintada = float(input('Digite os m² da área: '))

litros_necessarios = (area_pintada / 6) * 1.1

latas = math.ceil(litros_necessarios / 18)
preco_latas = latas * 80

galoes = math.ceil(litros_necessarios / 3.6 )
preco_galoes = galoes * 25

latas_mistura = int(litros_necessarios // 18)
resto = litros_necessarios - (latas_mistura * 18)

galoes_mistura = math.ceil(resto / 3.6)

preco_mistura = (latas_mistura * 80) + (galoes_mistura * 25)

print("\n--- OPÇÕES DE COMPRA ---")

print(f'\nApenas latas de 18L:')
print(f'{latas} latas - R$ {preco_latas:.2f}')

print(f'\nApenas galões de 3.6L:')
print(f'{galoes} galões - R$ {preco_galoes:.2f}')

print(f'\nMisturando latas e galões:')
print(f'{latas_mistura} latas e {galoes_mistura} galões')
print(f'Preço total: R$ {preco_mistura:.2f}')
