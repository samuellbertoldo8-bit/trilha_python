# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 01
#
# Enunciado:
#   Crie uma lista com 4 frutas e mostre-a na tela. Em seguida,
#   pratique os principais métodos de listas: append (adicionar),
#   remove (remover pelo valor), pop (remover o último), insert
#   (inserir em uma posição), sort (ordenar), reverse (inverter) e
#   clear (limpar).
# ====================================================================

#Variável frutas recebe 4 elementos
frutas = ["Maçã", "Laranja", "Banana", "Melância"]

print(frutas)

#Métodos responsável por atribuir funcionalidades nos vetores armazenados
frutas.append("Pera")      # Adiciona
frutas.remove("Banana")    # Remove pelo valor
frutas.pop()              # Remove o último valor
frutas.insert(1, "Uva")   # Insere em uma posição
frutas.sort()             # Ordena
frutas.reverse()          # Inverte
frutas.clear()            # Limpa a lista
