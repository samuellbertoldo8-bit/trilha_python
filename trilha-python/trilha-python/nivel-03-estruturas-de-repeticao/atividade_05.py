# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 05
#
# Enunciado:
#   Crie um programa em Python que leia 5 números e mostre a soma
#   entre eles (use uma variável acumuladora).
# ====================================================================

soma = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma = soma + numero

print(f"A soma dos números é {soma}")
