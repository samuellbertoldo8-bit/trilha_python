# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 11
#
# Enunciado:
#   Ranking de Games: leia o nome de 5 games, ordene a lista em
#   ordem alfabética e mostre os games numerados a partir de 1.
# ====================================================================

#Ranking de Games
#Cadastrar, ordenar e exibir numerados.
games = []

for i in range(5):
    game = input("Digite um game: ")
    games.append(game)

games.sort()

print("Ranking de Games:")

for i in range(len(games)):
    print(i + 1, "-", games[i])
