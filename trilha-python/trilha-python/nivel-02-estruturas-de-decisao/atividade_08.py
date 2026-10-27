# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 08
#
# Enunciado:
#   Crie um programa em Python que leia a velocidade de um carro e
#   informe se o motorista foi multado (velocidade acima de 80
#   km/h).
# ====================================================================

velocidade = float(input("Digite a velocidade: "))

if velocidade > 80:
    print("Motorista multado")
else:
    print("Velocidade permitida")
