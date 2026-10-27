# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 04
#
# Enunciado:
#   Crie uma função em Python chamada dobro(numero) que RETORNA
#   (return) o dobro de um número. Leia um número, chame a função e
#   mostre o resultado fora dela.
# ====================================================================

# 'numero' é o PARÂMETRO: o nome que o valor recebe DENTRO da função.
def dobro(numero):
    return numero * 2


valor = float(input("Digite um número: "))

# 'valor' é o ARGUMENTO: o que enviamos para a função na chamada.
# Os nomes podem ser diferentes: o Python copia o conteúdo de 'valor'
# para 'numero'. Se o usuário digitar 5, dentro da função numero = 5.
resultado = dobro(valor)

print(f"O dobro de {valor} é {resultado}")
