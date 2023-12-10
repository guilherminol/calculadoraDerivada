def derivadaGeral(polinomio):
    derivada = []

    for i in range(len(polinomio)-1):
        derivada.append(polinomio[i] * (len(polinomio) -1 -i))
    return derivada

def inputDerivada():
    derivada = []

    grau = int(input("Digite o grau da expressao: "))

    for i in range(grau + 1):
        if (grau - i) == 0:
            derivada.append(int(input(f"Digite o numero em que não há x -  ")))
        else:
            derivada.append(int(input(f"Digite o numero em que x tem grau {grau - i} -  ")))

    return derivada

def prettyDerivada(derivada):
    resultado = ''


    for index, value in enumerate(derivada):
        #Inverte o loop
        tamanho = (len(derivada) - 1)
        reverse_index = tamanho - index
        
        if value == 0:
            continue

        if value > 0:
            negativo = False
        else:
            negativo = True
            value = -value

        if negativo:
            resultado += f'- {value}'
        else:
            resultado += f'+ {value}'

        if reverse_index > 0:
            resultado += 'x'

        if reverse_index > 1:
            resultado += f'^{reverse_index}'   
        resultado += ' '
    return resultado