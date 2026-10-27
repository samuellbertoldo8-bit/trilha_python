# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 12
#
# Enunciado:
#   Desenvolva um programa em Python que mostre os números de 1 a
#   20, pulando os múltiplos de 3 (use continue).
# ====================================================================

for numero in range(1, 21):
    if numero % 3 == 0:
        continue

    print(numero)
