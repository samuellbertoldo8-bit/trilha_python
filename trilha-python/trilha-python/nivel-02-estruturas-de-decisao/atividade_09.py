# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 09
#
# Enunciado:
#   Desenvolva um programa em Python que leia o ano de nascimento de
#   uma pessoa, calcule sua idade (considerando o ano de 2026) e
#   informe se ela pode votar (16 anos ou mais).
# ====================================================================

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = 2026 - ano_nascimento

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")
