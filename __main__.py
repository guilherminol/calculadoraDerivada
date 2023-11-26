from menu import Menu
from derivadas import derivadaGeral


resposta = '0'

while (resposta != 9):
    resposta = Menu()

    if (resposta == 1):
        grau = int(input("Digite o grau da expressao: "))
        polinomio = []

        for i in range(grau):
            membroDaEquacao = input(f"Digite em que x tem grau {grau + 1 - i} -  ")
    


    # Exemplo de uso:
polinomio = [4,5,1]                                # representa 4xˆ2 + 5x + 1
print(derivadaGeral(polinomio)) # Saída: [8, 5], que representa 8x + 5

polinomio = [4,2,7,9]                                  # representa 4xˆ3 + 2xˆ2 + 7x + 9
print(derivadaGeral(polinomio)) # Saída: [12, 4, 7], que representa 12xˆ2 + 4x + 7

