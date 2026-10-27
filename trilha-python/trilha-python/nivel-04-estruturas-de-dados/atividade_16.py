# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 16
#
# Enunciado:
#   Leia 5 números inteiros, guarde-os em uma lista e mostre apenas
#   os números maiores que 10.
# ====================================================================

numeros = []

for i in range(5):

    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

print("Números maiores que 10:")

for numero in numeros:

    if numero > 10:
        print(numero)
