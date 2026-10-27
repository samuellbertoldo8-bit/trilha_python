# ====================================================================
# Nível 4 - Estruturas de Dados
# Atividade 20
#
# Enunciado:
#   Dicionários: crie um dicionário com os dados de um aluno (nome,
#   idade e curso). Mostre cada informação acessando pela chave,
#   altere a idade, adicione a chave 'cidade' e mostre o dicionário
#   atualizado.
#
# Exemplo de execução:
#   Nome: Ana
#   Idade: 17
#   Curso: Python
#   Dicionário atualizado:
#   {'nome': 'Ana', 'idade': 18, 'curso': 'Python', 'cidade': 'Guarulhos'}
# ====================================================================

# O dicionário é criado com CHAVES { } e guarda pares chave: valor
aluno = {
    "nome": "Ana",
    "idade": 17,
    "curso": "Python"
}

# Acessando os valores pela CHAVE (e não pela posição, como na lista)
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")
print(f"Curso: {aluno['curso']}")

# Alterando um valor que já existe
aluno["idade"] = 18

# Adicionando uma chave nova
aluno["cidade"] = "Guarulhos"

print("Dicionário atualizado:")
print(aluno)
