# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 02
#
# Enunciado:
#   Crie uma função em Python chamada saudacao(nome) que recebe o
#   nome de uma pessoa como parâmetro e mostra uma mensagem de boas-
#   vindas. Leia o nome do usuário e chame a função.
# ====================================================================

def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")


usuario = input("Digite seu nome: ")
saudacao(usuario)
