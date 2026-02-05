
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    print('Opções:')
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')

    escolha = input('Escolha uma opção: ')

    try: 
        escolha_int = int(escolha)
        if pergunta['Opções'][escolha_int] == pergunta['Resposta']:
            print('Acertou 👍🏼')
            acertos += 1
        else:
            print('Errou ❌')
    except:
        print('Opção inválida ❌')
    
    print('-' * 30)

print(f'Você acertou {acertos} de {len(perguntas)} perguntas')


