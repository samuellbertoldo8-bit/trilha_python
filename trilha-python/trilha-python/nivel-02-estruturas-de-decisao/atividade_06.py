# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 06
#
# Enunciado:
#   Desenvolva um programa em Python que leia a temperatura e
#   informe o clima: frio (abaixo de 18°C), agradável (de 18°C a
#   30°C) ou quente (acima de 30°C).
# ====================================================================

temperatura = float(input("Digite a temperatura: "))

if temperatura < 18:
    print("Clima frio")
elif temperatura <= 30:
    print("Clima agradável")
else:
    print("Clima quente")
