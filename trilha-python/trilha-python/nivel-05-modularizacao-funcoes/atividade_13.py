# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 13
#
# Enunciado:
#   Crie um programa em Python com duas funções:
#   calcular_area(largura, altura), que retorna a área de uma
#   parede, e calcular_tinta(largura, altura), que chama a primeira
#   função e retorna os litros de tinta necessários (1 litro para
#   cada 2m²). Leia as medidas e mostre a área e a tinta.
# ====================================================================

def calcular_area(largura, altura):
    return largura * altura


def calcular_tinta(largura, altura):
    area = calcular_area(largura, altura)   # uma função chamando outra
    return area / 2


largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

print(f"Área da parede: {calcular_area(largura, altura):.2f} m²")
print(f"Tinta necessária: {calcular_tinta(largura, altura):.2f} litros")
