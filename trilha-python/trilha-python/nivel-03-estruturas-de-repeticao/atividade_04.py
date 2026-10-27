# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 04
#
# Enunciado:
#   Faça um programa em Python que leia um número inteiro e mostre a
#   sua tabuada de multiplicação de 1 a 10.
# ====================================================================

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
