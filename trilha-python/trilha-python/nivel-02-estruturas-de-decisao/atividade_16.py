# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 16
#
# Enunciado:
#   Faça um programa em Python que leia a média final de um aluno e
#   mostre a situação: Aprovado (7 ou mais), Recuperação (de 5 a
#   6,9) ou Reprovado (abaixo de 5).
# ====================================================================

media = float(input("Digite a média final: "))

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
