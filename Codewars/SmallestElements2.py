def first_n_smallest(llistaNumeros, longitudLlista):
    resta = len(llistaNumeros)-longitudLlista
    llistaNumeros.reverse()
    for x in range(resta):
        llistaNumeros = llistaNumeros[:llistaNumeros.index(max(llistaNumeros))] + llistaNumeros[llistaNumeros.index(max(llistaNumeros))+1:]
    llistaNumeros.reverse()
    return llistaNumeros