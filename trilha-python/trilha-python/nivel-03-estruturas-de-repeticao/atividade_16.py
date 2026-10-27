# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 16
#
# Enunciado:
#   [DESAFIO] Faça um jogo de adivinhação em Python: o computador
#   sorteia um número de 1 a 100 e o usuário tenta adivinhar. A cada
#   palpite, o programa diz se o número secreto é maior ou menor.
#   Palpites fora de 1 a 100 ou que não sejam números devem ser
#   ignorados (use continue). Quando o usuário acertar, pare o jogo
#   (use break) e mostre quantas tentativas foram necessárias.
# ====================================================================

import random

secreto = random.randint(1, 100)
tentativas = 0

print("Pensei em um número de 1 a 100. Tente adivinhar!")

while True:
    palpite = input("Seu palpite: ")

    # Ignora o que não for número
    if not palpite.isdigit():
        print("Digite apenas números!")
        continue

    palpite = int(palpite)

    # Ignora números fora do intervalo
    if palpite < 1 or palpite > 100:
        print("O número deve estar entre 1 e 100!")
        continue

    tentativas = tentativas + 1

    if palpite == secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif palpite < secreto:
        print("O número secreto é MAIOR.")
    else:
        print("O número secreto é MENOR.")
