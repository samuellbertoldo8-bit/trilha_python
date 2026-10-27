# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 14
#
# Enunciado:
#   Crie uma função em Python chamada ler_nota(mensagem) que mostra
#   a mensagem recebida, pede uma nota ao usuário e só a retorna
#   quando ela estiver entre 0 e 10 (use while). Use a função para
#   ler duas notas e mostre a média.
# ====================================================================

def ler_nota(mensagem):
    nota = float(input(mensagem))

    while nota < 0 or nota > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        nota = float(input(mensagem))

    return nota


nota1 = ler_nota("Digite a primeira nota: ")
nota2 = ler_nota("Digite a segunda nota: ")

media = (nota1 + nota2) / 2

print(f"A média é {media:.2f}")
