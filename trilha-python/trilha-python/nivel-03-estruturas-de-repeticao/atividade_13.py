# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 13
#
# Enunciado:
#   Faça um programa em Python que mostre as tabuadas de 1 a 5
#   usando laços aninhados (um for dentro de outro for).
# ====================================================================

for numero in range(1, 6):
    print(f"--- Tabuada do {numero} ---")

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    print()
