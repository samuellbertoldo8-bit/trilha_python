# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 22
#
# Enunciado:
#   Lista de dicionários: cadastre 3 alunos, cada um com nome e
#   nota, guardando cada aluno em um dicionário dentro de uma lista.
#   No final, mostre todos os alunos cadastrados e a situação de
#   cada um (aprovado com nota maior ou igual a 6).
#
# Exemplo de execução:
#   Nome do 1º aluno: Ana
#   Nota de Ana: 8
#   Nome do 2º aluno: Bia
#   Nota de Bia: 5
#   Nome do 3º aluno: Caio
#   Nota de Caio: 6
#
#   === ALUNOS CADASTRADOS ===
#   Ana - Nota: 8.0 - Aprovado
#   Bia - Nota: 5.0 - Reprovado
#   Caio - Nota: 6.0 - Aprovado
# ====================================================================

alunos = []   # lista que vai guardar vários dicionários

for i in range(1, 4):
    nome = input(f"Nome do {i}º aluno: ")
    nota = float(input(f"Nota de {nome}: "))

    aluno = {"nome": nome, "nota": nota}   # um dicionário para cada aluno
    alunos.append(aluno)

print()
print("=== ALUNOS CADASTRADOS ===")

for aluno in alunos:
    if aluno["nota"] >= 6:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print(f"{aluno['nome']} - Nota: {aluno['nota']} - {situacao}")
