# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 09
#
# Enunciado:
#   Desenvolva um programa em Python que leia vários números. O
#   programa só para quando o usuário digitar 0 (use while True e
#   break). No final, mostre a soma e a quantidade de números
#   digitados (sem contar o 0).
# ====================================================================

soma = 0
quantidade = 0

while True:
    numero = float(input("Digite um número (0 para parar): "))

    if numero == 0:
        break

    soma = soma + numero
    quantidade = quantidade + 1

print(f"Você digitou {quantidade} números")
print(f"A soma deles é {soma}")
