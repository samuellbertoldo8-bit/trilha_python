# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 14
#
# Enunciado:
#   Crie um programa em Python que leia uma letra (M ou F) e mostre
#   o sexo correspondente: Masculino ou Feminino. Para qualquer
#   outra letra, mostre 'Opção inválida'.
# ====================================================================

sexo = input("Digite M ou F: ").upper()

if sexo == "M":
    print("Sexo Masculino")
elif sexo == "F":
    print("Sexo Feminino")
else:
    print("Opção inválida")
