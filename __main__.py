from menu import Menu
from derivadas import derivadaGeral, inputDerivada, prettyDerivada, derivada_trig_manual
from teste import multiplicarPolinomios, adicionarPolinomios


resposta = '0'

while (resposta != 9):
    resposta = Menu()

    if (resposta == 1):
        grau = int(input("Digite o grau da expressao: "))
        polinomio = []

        for i in range(grau):
            membroDaEquacao = input(f"Digite em que x tem grau {grau + 1 - i} -  ")
    
    if (resposta == 2):
        dividendo = []
        divisor = []

        print("Primeiro coloque a exepressão do DIVIDENDO:")
        # dividendo = [5, 8, 0, 2]
        dividendo = inputDerivada()

        print("Agora coloque a exepressão do DIVISOR:")
        # divisor = [3, 5, 1]
        divisor = inputDerivada()

        dividendo_derivada = derivadaGeral(dividendo)
        divisor_derivada = derivadaGeral(divisor)

        uv = multiplicarPolinomios(dividendo_derivada, divisor)
        vu = multiplicarPolinomios(dividendo, divisor_derivada)
        vu = [-i for i in vu]
        
        dividendo_operacao = adicionarPolinomios(uv, vu)
        divisor_operacao = divisor

        print(f'{prettyDerivada(dividendo_operacao)}/({prettyDerivada(divisor_operacao)})^2')

    if (resposta == 3):
        termo1 = []
        termo2 = []

        print("Primeiro coloque a exepressão do DIVIDENDO:")
        # termo1 = [5, 8, 0, 2]
        termo1 = inputDerivada()

        print("Agora coloque a exepressão do DIVISOR:")
        # termo2 = [3, 5, 1]
        termo2 = inputDerivada()

        termo1_derivada = derivadaGeral(termo1)
        termo2_derivada = derivadaGeral(termo2)

        uv = multiplicarPolinomios(termo1_derivada, termo2)
        vu = multiplicarPolinomios(termo1, termo2_derivada)

        produto = adicionarPolinomios(uv, vu)

        print(f'{prettyDerivada(produto)}')

    
    if (resposta == 4):
        funcTrig = input("Agora coloque a função trigonométrica (um termo por vez): ")
        print(f"Resultado: {derivada_trig_manual(funcTrig)}")

