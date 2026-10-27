# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 10
#
# Enunciado:
#   Escreva um programa em Python que demonstre o escopo de
#   variáveis: crie uma variável local dentro de uma função, uma
#   variável global fora dela, e uma função que altera a variável
#   global usando a palavra global.
# ====================================================================

pontos = 0   # variável GLOBAL: existe no programa inteiro


def mostrar_mensagem():
    mensagem = "Eu sou uma variável LOCAL"   # só existe dentro da função
    print(mensagem)
    print(f"Lendo a variável global dentro da função: pontos = {pontos}")


def ganhar_pontos(quantidade):
    global pontos   # avisa que vamos ALTERAR a variável global
    pontos = pontos + quantidade


mostrar_mensagem()

ganhar_pontos(10)
ganhar_pontos(5)

print(f"Pontos depois de chamar a função: {pontos}")

# Se tentar usar print(mensagem) aqui fora, dará erro,
# porque 'mensagem' é local e só existe dentro de mostrar_mensagem().

# 💡 Boa prática:
# Evite usar 'global'. Ele foi usado aqui só para demonstrar o escopo.
# Em programas maiores, alterar variáveis globais dentro de funções
# torna o código difícil de entender e de encontrar erros.
# O ideal é receber o valor por parâmetro e devolver com return:
#
# def ganhar_pontos(pontos, quantidade):
#     return pontos + quantidade
#
# pontos = ganhar_pontos(pontos, 10)
