# ====================================================================
# Nível 3 - Estruturas de Repetição
# Atividade 15
#
# Enunciado:
#   Desenvolva um programa em Python que simule um login: o usuário
#   tem no máximo 3 tentativas para acertar a senha (1234). Se
#   acertar, mostre 'Acesso permitido' e pare o laço com break. Se
#   errar as 3, mostre 'Conta bloqueada'.
# ====================================================================

senha_correta = "1234"
acertou = False

for tentativa in range(1, 4):
    senha = input(f"Tentativa {tentativa} de 3 - Digite a senha: ")

    if senha == senha_correta:
        acertou = True
        break

    print("Senha incorreta!")

if acertou:
    print("Acesso permitido")
else:
    print("Conta bloqueada")
