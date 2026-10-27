# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 10
#
# Enunciado:
#   Faça um programa em Python que leia 10 números inteiros e mostre
#   quantos são pares e quantos são ímpares (use variáveis
#   contadoras).
# ====================================================================

pares = 0
impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
