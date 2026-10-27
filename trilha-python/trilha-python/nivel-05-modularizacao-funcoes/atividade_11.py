# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 11
#
# Enunciado:
#   Crie uma função em Python chamada somar_lista(lista) que recebe
#   uma lista de números e retorna a soma de todos eles (sem usar a
#   função sum). Leia 5 números, guarde em uma lista e mostre a
#   soma.
# ====================================================================

def somar_lista(lista):
    total = 0

    for numero in lista:
        total = total + numero

    return total


numeros = []

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

print(f"A soma dos números é {somar_lista(numeros)}")

# 💡 Boa prática:
# Aqui a soma foi feita "na mão" para treinar o laço for.
# Na prática, o Python já tem uma função pronta para isso:
#
# total = sum(numeros)
