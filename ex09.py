palavra_secreta = 'carro'
palavras_adivinhada = ['*'] * len(palavra_secreta)
letras_tentadas =  []
tentativas = 0

print (f"Palavra secreta com{len(palavra_secreta)} letras: {''.join(palavras_adivinhada)}")
print("-" * 30)

while ''.join(palavras_adivinhada) != palavra_secreta:
    letra = input("\nDigite uma letra: ").lower().strip()

    if letra in letras_tentadas:
        print(f"A letra '{letra}' já foi tentada. Tente outra")
        continue

    letras_tentadas.append(letra)
    tentativas += 1

    if letra in palavra_secreta:
        print(f"Boa! a letra '{letra}' está na palavra")
        

        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavras_adivinhada[i] = letra
    else:
        print(f"A letra '{letra}' não esta na palvra")

    palavra_formatada = ''.join(palavras_adivinhada)
    print("-" * 30)
    print(f"Palavra formatada: {palavra_formatada}")
    print(f"Tentativas: {tentativas}")
    print(f"Letras já tentadas: {', '.join(letras_tentadas)}")
    print("-" * 30)


print("\n🎉 VOCÊ GANHOU PARABÉNS!!")
print(f"A palavra era: {palavra_secreta}")
print(f"Tentativas {tentativas}")
