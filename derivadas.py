def derivadaGeral(polinomio):
    derivada = []

    for i in range(len(polinomio)-1):
        derivada.append(polinomio[i] * (len(polinomio) -1 -i))
    return derivada


