# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 14
#
# Enunciado:
#   Desenvolva um programa em Python que leia Km percorridos e dias
#   de aluguel de um carro e calcule o valor total (R$90 por dia e
#   R$0,20 por Km).
# ====================================================================

dias = int(input("Digite a quantidade de dias: "))
km = float(input("Digite os quilômetros percorridos: "))

valor_dias = dias * 90
valor_km = km * 0.20

total = valor_dias + valor_km

print(f"O valor total do aluguel é R${total:.2f}")
