class Polinomio:
    potencia = 0

    def __init__(self, numero, potencia) -> None:
        self.potencia = potencia
        self.numero = numero
        self.tipo = 'Polinomio'
        if self.potencia == 0: self.tipo = 'Numero'
        if self.numero == 0: self.tipo = 'Desativado'

    def printPolinomio(self):
        if self.numero == 0:
            return None
        formated = ''
        if self.numero > 0:
            formated += f'+ {self.numero}'
        else:
            formated += f'- {-self.numero}'
        if self.potencia > 0:
            formated += 'x'
        if self.potencia > 1:
            formated += f'^{self.potencia}'

        return print(formated)

# Transforma a lista em uma lista de Classe: Polinomio
def formatarExpressao(lista):
    aux = []
    for index, value in enumerate(lista):
        reverse_index = len(lista) - 1 - index
        aux.append(Polinomio(value, reverse_index))
    return aux

def multiplicarPolinomios(expressao1, expressao2):
    expressao1 = formatarExpressao(expressao1)
    expressao2 = formatarExpressao(expressao2)

    # Faz o "chuveirinho" das expressões
    multiplicacao = []
    for polinomio_1 in expressao1:
        for polinomio_2 in expressao2:
            if 'Desativado' in (polinomio_1.tipo, polinomio_2.tipo):
                continue
            potencia = polinomio_1.potencia + polinomio_2.potencia
            numero = polinomio_1.numero * polinomio_2.numero
            multiplicacao.append(Polinomio(numero, potencia))

    # Verifica todas as potencias existentes
    potencias = []
    for polinomio in multiplicacao:
        # print(polinomio.printPolinomio())
        if polinomio.potencia not in potencias:
            potencias.append(polinomio.potencia)

    # Pega a maior potencia
    maior_potencia = -1
    for num in potencias:
        if num > maior_potencia: maior_potencia = num

    # Soma os polinomios de acordo com a potencia
    resultado = [0 for i in range(0, maior_potencia+1)]
    for index in range(0, maior_potencia+1):
        for polinomio in multiplicacao:
            if polinomio.potencia == index:
                resultado[index] += polinomio.numero
    resultado.reverse()
    # print(resultado)

    return resultado
    # print(resultado_formatado)
    # print([x.printPolinomio() for x in resultado])

def adicionarPolinomios(expressao1, expressao2):
    resultado = []

    if len(expressao1) < len(expressao2):
        maior = expressao2
        menor = expressao1
    else:
        maior = expressao1
        menor = expressao2

    for i in range(1, len(menor) + 1):
        i = -i
        resultado.append(maior[i] + menor[i])
    for i in range (len(menor) + 1, len(maior) + 1):
        i = -i
        resultado.append(maior[i])

    resultado.reverse()
    return resultado