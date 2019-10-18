def first_n_smallest(listaNumeros, longitudLista):
    listaOrdenada = listaNumeros[:]
    listaOrdenada.sort()
    if longitudLista == 0:
        return []
    if listaOrdenada == listaNumeros:
        return listaNumeros[0:longitudLista]
    if listaOrdenada != listaNumeros:
        resDesordenado = listaNumeros[0:longitudLista]
        for num in resDesordenado:
            if num in listaNumeros:
                comparacion = []
                comparacion.append(num)
            return comparacion


if __name__ == "__main__":  
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == []
    assert first_n_smallest([1, 2, 3, 4, 5], 0) == [1, 2, 3]
    assert first_n_smallest([5, 4, 3, 2, 1], 3) == [3, 2, 1]