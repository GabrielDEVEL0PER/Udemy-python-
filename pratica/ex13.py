arquivo = int(input("Digite o tamanho do seu arquivo (em MB): "))

internet_velocidade = float(input("Digite a velocidade da internet (em Mbps): "))

internet_calculo = internet_velocidade / 8

resultado = arquivo / internet_calculo

tempo = resultado / 60

print(f'Seu arquivo será baixado em {tempo:.2f} minutos')