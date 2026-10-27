# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 18
#
# Enunciado:
#   Votação de Participantes: leia os votos de uma eleição com 10
#   participantes (numerados de 1 a 10) e mostre quantos votos cada
#   participante recebeu, usando uma lista de contadores.
# ====================================================================

votos = []

# Recebe os 50 votos
for i in range(2):
    voto = int(input(f"Digite o voto {i+1}: "))
    votos.append(voto)

# Cria um vetor de contadores
# Criará 10 elementos recebendo 0 
# [0,0,0,0,0,0,0,0,0,0]
contador = [0] * 10

# Conta os votos
for voto in votos:
    contador[voto - 1] += 1

# Mostra o resultado
print("\nResultado da votação:")

for i in range(10):
    print(f"Participante {i+1}: {contador[i]} votos")
