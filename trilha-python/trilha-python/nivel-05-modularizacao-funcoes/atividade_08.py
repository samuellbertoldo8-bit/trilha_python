# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 08
#
# Enunciado:
#   Crie uma função em Python chamada calcular_preco(valor,
#   desconto=0) que retorna o preço final com desconto em
#   porcentagem. O desconto tem valor padrão 0, ou seja, se não for
#   informado, o preço não muda. Mostre o resultado chamando a
#   função com e sem desconto.
# ====================================================================

def calcular_preco(valor, desconto=0):
    valor_final = valor - (valor * desconto / 100)
    return valor_final


preco = float(input("Digite o preço do produto: "))

print(f"Sem desconto: R${calcular_preco(preco):.2f}")
print(f"Com 10% de desconto: R${calcular_preco(preco, 10):.2f}")
print(f"Com 25% de desconto: R${calcular_preco(preco, 25):.2f}")
