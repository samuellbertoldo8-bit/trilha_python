# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 16
#
# Enunciado:
#   [DESAFIO] Faça um programa em Python que calcule quantos dias de
#   vida um fumante perde, baseado na quantidade de cigarros por dia
#   e anos fumando.
# ====================================================================

cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

total_cigarros = cigarros_por_dia * 365 * anos_fumando

minutos_perdidos = total_cigarros * 10

dias_perdidos = minutos_perdidos / 1440

print(f"Você perdeu aproximadamente {dias_perdidos:.2f} dias de vida.")
