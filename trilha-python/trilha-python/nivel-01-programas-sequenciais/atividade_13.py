# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 13
#
# Enunciado:
#   Faça um programa em Python que leia o salário de um funcionário
#   e mostre o novo salário com 15% de aumento.
# ====================================================================

salario = float(input("Digite o salário: "))

aumento = salario * 0.15
novo_salario = salario + aumento

print(f"O novo salário é R${novo_salario:.2f}")
