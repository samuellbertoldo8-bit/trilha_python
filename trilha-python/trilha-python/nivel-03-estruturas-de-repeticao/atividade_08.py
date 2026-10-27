# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 08
#
# Enunciado:
#   Crie um programa em Python que leia uma nota entre 0 e 10.
#   Enquanto o usuário digitar uma nota inválida, o programa deve
#   mostrar uma mensagem de erro e pedir a nota novamente.
# ====================================================================

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida! Tente novamente.")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print(f"Nota registrada: {nota}")
