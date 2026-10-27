# ====================================================================
# Nível 2 - Estruturas de Decisão
# Atividade 11
#
# Enunciado:
#   Crie um programa em Python que leia um usuário e uma senha e
#   informe se o acesso foi permitido (senha correta: 1234) ou
#   negado.
# ====================================================================

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
