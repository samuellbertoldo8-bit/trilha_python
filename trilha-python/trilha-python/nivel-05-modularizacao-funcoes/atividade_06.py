# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 06
#
# Enunciado:
#   Crie uma função em Python chamada eh_par(numero) que retorna
#   True se o número for par e False se for ímpar. Leia um número e
#   use a função dentro de um if para mostrar o resultado.
# ====================================================================

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


valor = int(input("Digite um número inteiro: "))

if eh_par(valor):
    print(f"{valor} é par")
else:
    print(f"{valor} é ímpar")

# 💡 Boa prática:
# A comparação 'numero % 2 == 0' já resulta em True ou False,
# então a função pode ser escrita em uma única linha:
#
# def eh_par(numero):
#     return numero % 2 == 0
