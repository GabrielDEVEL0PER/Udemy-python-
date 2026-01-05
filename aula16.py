contador = 0

while contador <= 100:
    contador += 1

    if contador == 50:
        print('Não vou mostrar o 50')
        continue

    if contador >= 10 and contador <= 20:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 100:
        break
print('Acabou')
    
    