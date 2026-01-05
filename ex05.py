nome = input("Digite seu nome: ")

horas = input("Qual a hora atualmente: ")

try:
    horas = int(horas)

    if horas >= 0 and horas <= 11:
        print(f'Bom dia, {nome}')
    elif horas >= 12 and horas <= 17:
        print(f"Boa tarde, {nome}")
    elif horas >= 18 and horas <= 23:
        print(f"Boa noite, {nome}")
    else:
        print("Não conheço essa hora")
except ValueError:
    print('DIGITE APENAS NUMEROS INTEIROS!!')