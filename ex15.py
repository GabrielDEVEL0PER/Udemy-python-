# Crie uma nova lista chamada novos_funcionarios onde:

# Se o salário for maior que 2000, aumente 10%

# Senão, mantenha o salário igual

funcionarios = [
    {'nome': 'Ana', 'salario': 1500},
    {'nome': 'Bruno', 'salario': 2500},
    {'nome': 'Carlos', 'salario': 4000},
    {'nome': 'Daniela', 'salario': 1800},
]


# novos_funcionarios = []

# for funcionario in funcionarios:
#     if funcionario['salario'] > 2000:
#         novo = {
#             **funcionario,
#             'salario': funcionario['salario'] * 1.10
#         }
#     else:
#         novo = {**funcionario}
#     novos_funcionarios.append(novo)
# print(novos_funcionarios)

novos_funcionarios = [
    {**funcionario, 'salario': funcionario['salario'] * 1.10}
    if funcionario['salario'] > 2000
    else {**funcionario}
    for funcionario in funcionarios
]

print(novos_funcionarios)