ganha_por_hora = float(input("Quanta ganha por hora: "))

horas_trabalhadas_no_mes = int(input("Horas trabalhadas no mês: "))

salario_bruto = horas_trabalhadas_no_mes * ganha_por_hora

imposto_de_renda = salario_bruto * 0.11

inss = salario_bruto * 0.08

sindicato = salario_bruto * 0.05

descontos = imposto_de_renda + inss + sindicato

salario_liquido = salario_bruto - descontos


print(f'Seu salario bruto é {salario_bruto}, porém com descontos fica {salario_liquido} \n Você pagou de INSS {inss}, de SINDICATO {sindicato}')