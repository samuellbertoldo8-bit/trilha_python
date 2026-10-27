# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 12
#
# Enunciado:
#   Crie um programa em Python que leia o preço de um produto e
#   mostre o valor com 5% de desconto.
# ====================================================================

preco = float(input("Digite o preço do produto: "))

desconto = preco * 0.05
novo_preco = preco - desconto

print(f"O valor com desconto é R${novo_preco:.2f}")
