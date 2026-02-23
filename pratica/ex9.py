peso_dos_peixes = float(input("Digite o peso do seu peixe: "))
 

excesso = 0
multa = 0

if peso_dos_peixes > 50:
    excesso = peso_dos_peixes - 50
    multa = excesso * 4 
    print(f'Seu peixe passou {excesso} kg a mais. E pagará de {multa} ')
else:
    print('Seu peixe está no peso')

