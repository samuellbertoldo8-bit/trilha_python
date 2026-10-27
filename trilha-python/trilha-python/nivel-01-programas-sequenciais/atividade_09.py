# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 09
#
# Enunciado:
#   Crie um programa em Python que leia quanto dinheiro uma pessoa
#   tem e mostre quantos dólares ela pode comprar (considere 1 dólar
#   = R$3,45).
# ====================================================================

valor = float(input("Quanto você recebe:"))

dolar = 3.45

resultado = valor / dolar

print(f"Ela poderá comprar {resultado} dólares")
