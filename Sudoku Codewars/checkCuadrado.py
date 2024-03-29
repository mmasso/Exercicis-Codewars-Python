def checkCuadrado(sudoku):
    assert isinstance(sudoku, list)
    if len(sudoku) == 3:
        contadorTrue = 0
        for fila in sudoku:
            if len(fila) != len(sudoku):
                return False
    return True
    assert checkCuadrado(sudoku) == bool


if __name__ == "__main__":
    assert checkCuadrado([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True
    assert checkCuadrado([[1, 2, 3, 4],
                          [2, 3, 1, 3],
                          [3, 1, 2, 3],
                          [4, 4, 4, 2]]) == True
    assert checkCuadrado([[1, 2, 3, 4, 5],
                          [2, 3, 1, 5, 6],
                          [4, 5, 2, 1, 3],
                          [3, 4, 5, 2, 1],
                          [5, 6, 4, 3, 2]]) == True
    assert checkCuadrado([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1]]) == False
    assert checkCuadrado([[]]) == True
