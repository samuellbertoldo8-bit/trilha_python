# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 23
#
# Enunciado:
#   Conjuntos: a partir de uma lista de games com nomes repetidos,
#   use um conjunto (set) para remover as repetições. Depois, com os
#   games favoritos de dois amigos, mostre os games que os dois
#   gostam (interseção) e todos os games sem repetir (união).
#
# Exemplo de execução:
#   Lista original: ['Minecraft', 'Roblox', 'Minecraft', 'GTA', 'Roblox', 'Minecraft']
#   Sem repetições: {'Minecraft', 'GTA', 'Roblox'}
#   Quantidade de games diferentes: 3
#   Games que os dois gostam: {'Minecraft', 'GTA'}
#   Todos os games, sem repetir: {'Minecraft', 'Roblox', 'Fortnite', 'GTA'}
#   (a ordem dentro das chaves { } pode mudar, pois conjuntos não têm ordem)
# ====================================================================

# O conjunto (set) também usa CHAVES { }, mas só com valores (sem chave: valor)
# e NÃO aceita elementos repetidos.

games = ["Minecraft", "Roblox", "Minecraft", "GTA", "Roblox", "Minecraft"]

print(f"Lista original: {games}")

sem_repetidos = set(games)   # transforma a lista em conjunto

print(f"Sem repetições: {sem_repetidos}")
print(f"Quantidade de games diferentes: {len(sem_repetidos)}")

# Atenção: o conjunto NÃO tem ordem, então os games podem
# aparecer em uma ordem diferente a cada execução.

amigo1 = {"Minecraft", "GTA", "Fortnite"}
amigo2 = {"Roblox", "GTA", "Minecraft"}

print(f"Games que os dois gostam: {amigo1 & amigo2}")   # interseção
print(f"Todos os games, sem repetir: {amigo1 | amigo2}")   # união
