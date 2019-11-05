def checkFilas(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        for (posicion, numero) in enumerate(fila):
            if numero in fila[posicion + 1:]:
                return False

    return True


if __name__ == '__main__':
    assert checkFilas([[1, 2, 3, 4],
                       [2, 3, 1, 3],
                       [3, 1, 2, 3],
                       [4, 4, 4, 2]]) == False
    assert checkFilas([[1, 2, 3],
                       [2, 3, 1],
                       [3, 1, 2]]) == True
    assert checkFilas([[1, 2, 3, 4],
                       [2, 3, 4, 1],
                       [3, 4, 1, 2],
                       [4, 1, 2, 3]]) == True
