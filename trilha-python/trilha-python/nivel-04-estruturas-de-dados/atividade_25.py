# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 25
#
# Enunciado:
#   [DESAFIO] Sistema de Biblioteca Gamer: cadastre 5 games em uma
#   lista e permita que o usuário pesquise quantos games quiser,
#   informando se cada um está disponível. O programa só termina
#   quando o usuário digitar 'sair'.
# ====================================================================

#Sistema de Biblioteca Gamer (Desafio)
#Cadastrar jogos e permitir consultas até o usuário decidir parar.


games = []

for i in range(5):
    game = input("Digite um game: ")
    games.append(game)

while True:

    pesquisa = input("Pesquisar game (ou sair): ")

    if pesquisa.lower() == "sair":
        break

    if pesquisa in games:
        print("Game disponível!")
    else:
        print("Game não encontrado.")
