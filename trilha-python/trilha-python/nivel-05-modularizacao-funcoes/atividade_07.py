# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 07
#
# Enunciado:
#   Crie uma função em Python chamada maior_de_tres(a, b, c) que
#   retorna o maior entre três números. Leia os três números e
#   mostre o maior.
# ====================================================================

def maior_de_tres(a, b, c):
    maior = a

    if b > maior:
        maior = b
    if c > maior:
        maior = c

    return maior


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f"O maior número é {maior_de_tres(n1, n2, n3)}")
