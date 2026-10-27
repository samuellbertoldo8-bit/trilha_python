# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 05
#
# Enunciado:
#   Crie uma função em Python chamada calcular_media(nota1, nota2)
#   que retorna a média de duas notas. Leia as notas, use a função e
#   mostre a média.
# ====================================================================

def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media_final = calcular_media(n1, n2)

print(f"A média é {media_final:.2f}")
