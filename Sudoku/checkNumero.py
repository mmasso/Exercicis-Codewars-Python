def numEnteros(sudoku):

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                return False

    return True


def numRango(sudoku):

    numValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if numero not in numValidos:
                return False

    return True


def checkNumero(sudoku):

    validez = numEnteros(sudoku) and numRango(sudoku)

    return validez


if __name__ == '__main__':
    assert checkNumero([[1, 2, 3], [2, 3, 1], [3, 1, 2]]) == True
    assert checkNumero([[1, 2, 3, 4],
                        [2, 3, 1, 3],
                        [3, 1, 2, 3],
                        [4, 4, 4, 2]]) == True
    assert checkNumero([[1, 2, 3, 4, 5],
                        [2, 3, 1, 5, 6],
                        [4, 5, "-", 1, 3],
                        [3, 4, 5, 2, 1],
                        [5, 6, 4, 3, 2]]) == False
    assert checkNumero([[1, 2, 3],
                        [2, 3, 1],
                        [3, 1, -5]]) == False
    assert checkNumero([["-"]]) == False
    assert checkNumero([[1, "i", 3, 4],
                        [2, 3, 1, 3],
                        [3, 1, 2, 3],
                        [4, 4, 4, 2]]) == False
