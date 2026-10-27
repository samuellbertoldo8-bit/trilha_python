# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 14
#
# Enunciado:
#   Game Favorito: leia o game favorito de 5 pessoas e guarde-os em
#   uma lista. Depois, peça o nome de um game e mostre quantas vezes
#   ele aparece usando o método count().
# ====================================================================

#Game Favorito
#Perguntar qual é o jogo favorito da turma e contar quantas vezes ele aparece.

games = []

for i in range(5):
    game = input("Digite seu game favorito: ")
    games.append(game)

favorito = input("Qual game deseja contar? ")

quantidade = games.count(favorito)

print("O game", favorito, "apareceu", quantidade, "vezes.")
