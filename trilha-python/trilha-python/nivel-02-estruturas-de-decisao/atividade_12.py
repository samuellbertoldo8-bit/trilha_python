# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 12
#
# Enunciado:
#   Desenvolva um programa em Python que leia a quantidade de faltas
#   de um aluno e informe se ele foi reprovado por faltas (mais de
#   25 faltas) ou aprovado por frequência.
# ====================================================================

faltas = int(input("Digite a quantidade de faltas: "))

if faltas > 25:
    print("Reprovado por faltas")
else:
    print("Aprovado por frequência")
