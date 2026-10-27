# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 14
#
# Enunciado:
#   Crie um programa em Python que leia um número inteiro e calcule
#   o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120.
# ====================================================================

numero = int(input("Digite um número: "))

fatorial = 1

for i in range(numero, 0, -1):
    fatorial = fatorial * i

print(f"{numero}! = {fatorial}")
