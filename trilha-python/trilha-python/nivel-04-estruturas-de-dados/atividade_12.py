# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 12
#
# Enunciado:
#   Remover um Game: mostre uma lista de games, peça ao usuário o
#   nome de um game para remover e, se ele existir, remova-o. Mostre
#   a lista no final.
# ====================================================================

#Remover um Game
#Permitir que o usuário exclua um jogo da lista.

games = ["Minecraft", "Valorant", "Roblox", "Fortnite"]

print(games)

remover = input("Qual game deseja remover? ")

if remover in games:
    games.remove(remover)
    print("Game removido com sucesso!")
else:
    print("Game não encontrado!")

print(games)
