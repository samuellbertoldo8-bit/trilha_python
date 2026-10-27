# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 17
#
# Enunciado:
#   Votação de Games: a partir de uma lista com 5 games, leia 5
#   votos (de 1 a 5, de acordo com a posição de cada game) e mostre
#   quantos votos cada game recebeu, usando uma lista de contadores.
# ====================================================================

votacaoJogos = []
games = ["Minecraft", "Roblox", "Valorant", "Fortnite", "Free Fire"]

for i in range(5):

    votacao = int(input("Digite o valor de acordo com o game de sua preferência: "))
    votacaoJogos.append(votacao)

contador = [0] * 5

for voto in votacaoJogos:
    contador[voto - 1] += 1

print("\nResultado da votação:")

for i in range(len(games)):
    print(games[i], ":", contador[i], "votos")
