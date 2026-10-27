# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 12
#
# Enunciado:
#   Crie uma função em Python chamada maior_e_menor(lista) que
#   recebe uma lista de números e retorna dois valores ao mesmo
#   tempo: o maior e o menor. Leia 5 números e mostre os dois
#   resultados.
# ====================================================================

def maior_e_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    return maior, menor   # retorna dois valores


numeros = []

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

maior, menor = maior_e_menor(numeros)   # recebe os dois valores

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")

# 💡 Boa prática:
# A busca foi feita "na mão" para treinar a lógica.
# Na prática, o Python já tem funções prontas para isso:
#
# maior = max(numeros)
# menor = min(numeros)
