# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 06
#
# Enunciado:
#   Desenvolva um programa em Python que leia as 4 notas de um aluno
#   e mostre a média.
# ====================================================================

soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma = soma + nota

media = soma / 4

print(f"A média do aluno é {media:.2f}")
