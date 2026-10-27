# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 15
#
# Enunciado:
#   Crie uma lista de games, leia o nome de um game escolhido pelo
#   usuário e informe se ele está na lista.
# ====================================================================

game = ["GTA", "Fifa 24", "Pes 2026", "Dead Space", "DeadSpace 2 "]

jogador = input("Digite o nome do game escolhido ?")

game.append(jogador)

if "GTA" in jogador:
    
    print("Está na lista")
    
else:
    
    print("Não está na lista")
