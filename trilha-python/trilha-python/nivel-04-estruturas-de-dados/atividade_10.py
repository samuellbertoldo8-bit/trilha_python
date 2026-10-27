# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 10
#
# Enunciado:
#   Procurar um Game: leia o nome de 5 games e guarde-os em uma
#   lista. Depois, peça o nome de um game e informe se ele foi
#   encontrado na lista.
# ====================================================================

#Procurar um Game
#O aluno cadastra jogos e depois pesquisa um deles.

games = []

for i in range(5):
    game = input("Digite um game: ")
    games.append(game)

pesquisa = input("Qual game deseja procurar? ")

if pesquisa in games:
    print("Game encontrado!")
else:
    print("Game não encontrado!")
