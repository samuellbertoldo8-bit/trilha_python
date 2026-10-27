# ====================================================================
# Nível 1 - Programas Sequenciais
# Atividade 08
#
# Enunciado:
#   Faça um programa em Python que leia uma distância em metros e
#   mostre os valores em km, hm, dam, dm, cm e mm.
# ====================================================================

metro = float(input("Digite uma disstÂncioa em metros:"))


km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print("Quilômetros:", km)
print("Hectômetros:", hm)
print("Decâmetros:", dam)
print("Decímetros:", dm)
print("Centímetros:", cm)
print("Milímetros:", mm)
