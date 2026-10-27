# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 07
#
# Enunciado:
#   Cadastro de Games: leia o nome de 4 games informados pelo
#   usuário, guarde-os em uma lista e mostre todos os games
#   cadastrados.
# ====================================================================

#Cadastro de Games
#Cadastrar 4 games informados pelo usuário.
games = []

for i in range(4):
    game = input("Digite o nome de um game: ")
    games.append(game)

print("Games cadastrados:")
print(games)
