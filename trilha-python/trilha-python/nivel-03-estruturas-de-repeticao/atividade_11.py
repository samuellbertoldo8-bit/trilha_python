# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 11
#
# Enunciado:
#   Crie um programa em Python que leia 5 números e mostre qual foi
#   o maior e qual foi o menor valor digitado.
# ====================================================================

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))

    if i == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
