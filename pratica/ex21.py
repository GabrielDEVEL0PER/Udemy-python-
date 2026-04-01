# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

produto1 = float(input("QUAL O PREÇO: "))

produto2 = float(input("QUAL O PREÇO: "))

produto3 = float(input("QUAL O PREÇO: "))

if produto1 <= produto2 and produto1 <= produto3:
    print(f'O mais barato é o produto 1, custando{produto1}')

elif produto2 <= produto1 and produto2 <= produto3:
    print(f'O mais barato é o produto 2, custando {produto2}')

else:
    print(f'O mais barato é o produto 3, custando {produto3}')