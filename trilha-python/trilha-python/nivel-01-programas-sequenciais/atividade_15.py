# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 15
#
# Enunciado:
#   Crie um programa em Python que leia o número de dias trabalhados
#   e calcule o salário (8h por dia, R$25 por hora).
# ====================================================================

dias = int(input("Digite a quantidade de dias trabalhados: "))

horas = dias * 8
salario = horas * 25

print(f"O salário é R${salario:.2f}")
