# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 08
#
# Enunciado:
#   Crie uma lista de games e mostre a posição (índice) e o nome de
#   cada um.
# ====================================================================

#Mostrar posição e nome do Game
#Exibir o índice e o nome de cada jogo.

games = ["Minecraft", "Free Fire", "Fortnite", "Roblox"]

for i in range(len(games)):
    print(i, "-", games[i])
