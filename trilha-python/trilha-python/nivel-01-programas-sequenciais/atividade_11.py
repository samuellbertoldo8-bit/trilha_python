# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 11
#
# Enunciado:
#   Desenvolva um programa em Python que leia os valores de A, B e C
#   e calcule o valor de Delta.
# ====================================================================

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c

print(f"O valor de Delta é {delta}")
