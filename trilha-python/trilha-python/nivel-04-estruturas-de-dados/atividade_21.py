# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 21
#
# Enunciado:
#   Dicionários: crie um dicionário com o estoque de uma loja de
#   games (nome do game: quantidade). Percorra o dicionário com for
#   usando items() para mostrar cada game e sua quantidade, e
#   verifique se um game digitado pelo usuário existe no estoque.
#
# Exemplo de execução:
#   === ESTOQUE ===
#   Minecraft: 10 unidades
#   Roblox: 5 unidades
#   Fortnite: 0 unidades
#   Valorant: 8 unidades
#   Qual game deseja procurar? Roblox
#   Roblox está no estoque com 5 unidades.
# ====================================================================

estoque = {
    "Minecraft": 10,
    "Roblox": 5,
    "Fortnite": 0,
    "Valorant": 8
}

print("=== ESTOQUE ===")

# items() devolve a chave e o valor ao mesmo tempo
for game, quantidade in estoque.items():
    print(f"{game}: {quantidade} unidades")

# Outras formas de percorrer:
# estoque.keys()   -> só as chaves (nomes dos games)
# estoque.values() -> só os valores (quantidades)

pesquisa = input("Qual game deseja procurar? ")

# O operador in verifica se a CHAVE existe no dicionário
if pesquisa in estoque:
    print(f"{pesquisa} está no estoque com {estoque[pesquisa]} unidades.")
else:
    print(f"{pesquisa} não existe no estoque.")
