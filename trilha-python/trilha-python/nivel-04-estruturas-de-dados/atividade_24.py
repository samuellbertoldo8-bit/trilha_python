# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 24
#
# Enunciado:
#   Comparando as estruturas: crie uma lista, uma tupla, um
#   dicionário e um conjunto com informações de games e mostre a
#   principal diferença entre eles: a lista pode ser alterada, a
#   tupla não, o dicionário guarda chave e valor, e o conjunto não
#   aceita repetidos.
#
# Exemplo de execução:
#   Lista (pode alterar): ['Valorant', 'Roblox', 'GTA', 'Fortnite']
#   Tupla (não pode alterar): ('Minecraft', 'Roblox', 'GTA')
#   Dicionário (chave: valor): {'nome': 'Minecraft', 'genero': 'Aventura', 'nota': 9.5}
#   Gênero do game: Aventura
#   Conjunto (sem repetidos): {'Roblox', 'GTA', 'Minecraft'}
# ====================================================================

# LISTA [ ]: ordenada e pode ser alterada
lista_games = ["Minecraft", "Roblox", "GTA"]
lista_games[0] = "Valorant"
lista_games.append("Fortnite")
print(f"Lista (pode alterar): {lista_games}")

# TUPLA ( ): ordenada, mas NÃO pode ser alterada
tupla_games = ("Minecraft", "Roblox", "GTA")
print(f"Tupla (não pode alterar): {tupla_games}")
# tupla_games[0] = "Valorant"  -> daria ERRO

# DICIONÁRIO {chave: valor}: acessa os dados pelo nome da chave
dicionario_game = {"nome": "Minecraft", "genero": "Aventura", "nota": 9.5}
print(f"Dicionário (chave: valor): {dicionario_game}")
print(f"Gênero do game: {dicionario_game['genero']}")

# CONJUNTO { }: não aceita repetidos e não tem ordem
conjunto_games = {"Minecraft", "Roblox", "Minecraft", "GTA"}
print(f"Conjunto (sem repetidos): {conjunto_games}")

# Resumo:
# | Estrutura  | Símbolo        | Tem ordem? | Pode alterar? | Aceita repetidos? |
# | Lista      | [ ]            | Sim        | Sim           | Sim               |
# | Tupla      | ( )            | Sim        | Não           | Sim               |
# | Dicionário | {chave: valor} | Sim        | Sim           | Chaves não        |
# | Conjunto   | { }            | Não        | Sim           | Não               |
