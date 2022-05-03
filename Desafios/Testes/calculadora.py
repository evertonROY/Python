# Imprime uma linha contendo n + 2 caracteres #
def print_linha(n):
    for i in range(n + 2):
        print("#", end="")
    print()

# Recebe uma string e imprime no formato
# #################
#  valor da string
# #################
def print_cabecalho(s):
    n = len(s)
    print_linha(n)
    print(" " + s)
    print_linha(n)

# Imprime o menu e retorna a opção escolhida pelo usuário
def input_opcao():
    print_cabecalho("Programa Calculadora v2.0")
    print(" 1. Soma")
    print(" 2. Subtração")
    print(" 3. Sair")
    opcao = input()
    return opcao

opcao = input_opcao()
while opcao != "3":
    if opcao == "1":
        print_cabecalho("Soma")
        print("Digite dois números separados por espaço:")
        x, y = map(float, input().split())
        print("A soma é igual a", (x + y))
    elif opcao == "2":
        print_cabecalho("Subtração")
        print("Digite dois números separados por espaço:")
        x, y = map(float, input().split())
        print("A diferença é igual a", (x - y))

    opcao = input_opcao()
        
print("Até logo!")