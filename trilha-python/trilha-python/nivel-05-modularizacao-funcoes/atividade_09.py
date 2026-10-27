# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 09
#
# Enunciado:
#   Crie uma função em Python chamada mostrar_ficha(nome, idade,
#   cidade) que mostra os dados de uma pessoa. Chame a função usando
#   argumentos nomeados (exemplo: cidade='Guarulhos'), inclusive
#   fora da ordem dos parâmetros.
# ====================================================================

def mostrar_ficha(nome, idade, cidade):
    print("--- FICHA ---")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")


# Argumentos posicionais (na ordem dos parâmetros)
mostrar_ficha("Ana", 25, "São Paulo")

# Argumentos nomeados (a ordem não importa)
mostrar_ficha(cidade="Guarulhos", nome="Carlos", idade=30)
