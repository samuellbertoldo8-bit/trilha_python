# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 13
#
# Enunciado:
#   Quantidade de Games: leia o nome de 5 games, guarde-os em uma
#   lista e mostre quantos games foram cadastrados usando len().
# ====================================================================

#Quantidade de Games
#Mostrar quantos jogos existem na lista.

games = []

for i in range(5):
    game = input("Digite um game: ")
    games.append(game)

print("Quantidade de games cadastrados:", len(games))
