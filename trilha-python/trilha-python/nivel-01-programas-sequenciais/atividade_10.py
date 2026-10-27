# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 10
#
# Enunciado:
#   Faça um programa em Python que leia a largura e altura de uma
#   parede, calcule a área e a quantidade de tinta necessária (1
#   litro para cada 2m²).
# ====================================================================

largura = float(input("Digite a largura:"))
altura = float(input("Dgite a altura:"))

area = largura * altura
tinta = area * 2 


print(f"A área da parede é {area:.2f} m²")
print(f"Serão necessários {tinta:.2f} litros de tinta")
