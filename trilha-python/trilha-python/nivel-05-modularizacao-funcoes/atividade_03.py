# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 03
#
# Enunciado:
#   Crie uma função em Python chamada mostrar_soma(n1, n2) que
#   recebe dois números e mostra a soma entre eles. Leia dois
#   números e chame a função.
# ====================================================================

def mostrar_soma(n1, n2):
    soma = n1 + n2
    print(f"A soma de {n1} + {n2} é {soma}")


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

mostrar_soma(numero1, numero2)
