def checkColumnas(sudoku):
    assert isinstance(sudoku, list)
    numeroDeFilas = len(sudoku)
    indexFilaActual = 0
    for fila in sudoku:
        for numero in fila:
            indexFilaSiguiente = indexFilaActual + 1
            while indexFilaSiguiente < numeroDeFilas:
                try:
                    posicionNumeroFilaSiguiente = sudoku[
                        indexFilaSiguiente].index(numero)
                except ValueError:
                    return False
                else:
                    if posicionNumeroFilaSiguiente == fila.index(numero):
                        return False
                    else:
                        indexFilaSiguiente += 1
        indexFilaActual += 1
    return True


if __name__ == '__main__':
    assert checkColumnas([[1, 2, 3, 4],
                         [2, 3, 1, 3],
                         [3, 1, 2, 3],
                         [4, 4, 4, 2]]) == False
    assert checkColumnas([[1, 2, 3],
                         [2, 3, 1],
                         [3, 1, 2]]) == True
    assert checkColumnas([[1, 2, 3, 4],
                         [2, 3, 4, 1],
                         [3, 4, 1, 2],
                         [4, 1, 2, 3]]) == True
