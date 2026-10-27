# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 07
#
# Enunciado:
#   Faça um programa em Python que leia o salário de um funcionário
#   e informe se ele receberá aumento (somente salários abaixo de
#   R$2.000).
# ====================================================================

salario = float(input("Digite o salário: "))

if salario < 2000:
    print("Receberá aumento")
else:
    print("Não receberá aumento")
