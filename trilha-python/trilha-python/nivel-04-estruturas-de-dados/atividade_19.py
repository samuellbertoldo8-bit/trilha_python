# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 19
#
# Enunciado:
#   Tuplas: crie uma tupla com os 7 dias da semana, mostre o
#   primeiro e o último dia, a quantidade de dias e percorra a tupla
#   com for. Depois, explique por que não é possível alterar um
#   elemento de uma tupla.
#
# Exemplo de execução:
#   Primeiro dia: Domingo
#   Último dia: Sábado
#   Quantidade de dias: 7
#   Dias da semana:
#   Domingo
#   Segunda
#   ... (até Sábado)
# ====================================================================

# A tupla é criada com PARÊNTESES ( )
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

print(f"Primeiro dia: {dias[0]}")
print(f"Último dia: {dias[-1]}")      # índice -1 = último elemento
print(f"Quantidade de dias: {len(dias)}")

print("Dias da semana:")
for dia in dias:
    print(dia)

# A tupla é IMUTÁVEL: depois de criada, não pode ser alterada.
# Se tentar fazer isto, o Python mostra um erro (TypeError):
#
# dias[0] = "Feriado"
#
# Use tupla quando os dados NÃO devem mudar,
# como os dias da semana, os meses do ano ou coordenadas.
