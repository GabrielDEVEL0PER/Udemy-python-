# Tendo como dados de entrada um arquivo em 
# Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:

giga = float(input("Digite o tamanho do arquivo: "))

conversor = giga * 1024

print(f"valor em megas é {conversor}")