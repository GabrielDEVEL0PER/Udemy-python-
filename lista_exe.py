import os 

compras = []

while True: 
    print('Selecione uma opção')
    opcao = input('[i] inserir [a] apagar [l] listar: ').lower()

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        compras.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del compras[indice]
        except ValueError:
            print('Por favor, digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        if len(compras) == 0:
            print('Nada para listar')

        for indice, nome in enumerate(compras):
            print(indice, nome)
    else:
        print('Por favor, escolha i, a ou l')