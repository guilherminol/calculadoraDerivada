def Menu():
    print("Bem vindo a Calculadora, escolha uma opção: ")
    printaBarras()
    print("1 - Derivada simples")
    print("9 - Sair")
    resultado = int( input('') )
    return resultado


def printaBarras():
    print("------------------------------------------")