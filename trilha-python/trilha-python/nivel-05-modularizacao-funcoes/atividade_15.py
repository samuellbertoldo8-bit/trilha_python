# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 15
#
# Enunciado:
#   Crie funções lambda (funções anônimas de uma linha) em Python
#   para calcular o quadrado de um número e a soma de dois números.
#   Depois, use uma lambda para ordenar uma lista de games pelo
#   tamanho do nome.
# ====================================================================

# Uma lambda é uma função pequena, escrita em uma única linha
quadrado = lambda x: x ** 2
somar = lambda a, b: a + b

print(f"Quadrado de 5: {quadrado(5)}")
print(f"Soma de 3 + 7: {somar(3, 7)}")

# Equivalente, com def:
# def quadrado(x):
#     return x ** 2

games = ["Minecraft", "GTA", "Roblox", "Free Fire", "Valorant"]

# key indica o critério de ordenação: aqui, o tamanho do nome
games.sort(key=lambda nome: len(nome))

print("Games ordenados pelo tamanho do nome:")
print(games)

# 💡 Boa prática:
# 1) O guia de estilo do Python (PEP 8) recomenda NÃO guardar uma lambda
#    em uma variável, como em 'quadrado = lambda x: x ** 2'. Nesse caso,
#    use def. A lambda foi guardada aqui só para mostrar como ela funciona.
#
# 2) A lambda é ideal quando usada direto, como no key do sort().
#    E, neste exemplo, a função len já faz o trabalho sozinha:
#
#    games.sort(key=len)
