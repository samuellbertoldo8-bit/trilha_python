# ====================================================================
# Nível 5 - Modularização (Funções)
# Atividade 16
#
# Enunciado:
#   [DESAFIO] Crie uma calculadora em Python totalmente organizada
#   em funções: uma função para mostrar o menu, uma para cada
#   operação (somar, subtrair, multiplicar e dividir) e uma função
#   principal. O programa deve repetir até o usuário escolher sair,
#   avisar quando a opção for inválida e impedir a divisão por zero.
# ====================================================================

def mostrar_menu():
    print()
    print("=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None   # sinaliza que a divisão não é possível
    return a / b


def ler_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b


def principal():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Calculadora encerrada. Até logo!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida!")
            continue

        a, b = ler_numeros()

        if opcao == "1":
            print(f"Resultado: {somar(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {subtrair(a, b)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicar(a, b)}")
        else:
            resultado = dividir(a, b)
            if resultado is None:
                print("Erro: não é possível dividir por zero!")
            else:
                print(f"Resultado: {resultado}")


# 💡 Boa prática:
# Em vez de chamar principal() direto, o padrão profissional é:
#
# if __name__ == "__main__":
#     principal()
#
# Isso faz o programa rodar só quando este arquivo é executado,
# e não quando ele é importado por outro arquivo (assunto de módulos).
principal()
