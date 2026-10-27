# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 15
#
# Enunciado:
#   Desenvolva um programa em Python que leia o preço de um produto
#   e calcule o valor final com desconto: 10% para produtos acima de
#   R$100 e 5% para os demais.
# ====================================================================

preco = float(input("Digite o preço do produto: "))

if preco > 100:
    desconto = preco * 0.10
else:
    desconto = preco * 0.05

valor_final = preco - desconto

print(f"Valor final: R${valor_final:.2f}")
