from checkColumnas import checkColumnas
from checkCuadrado import checkCuadrado
from checkFilas import checkFilas
from checkNumero import checkNumero
from checkTresxTres import checkTresxTres


def check_sudoku(sudoku):
    validezSudoku = checkCuadrado(sudoku) and checkNumero(sudoku) \
        and checkFilas(sudoku) and checkColumnas(sudoku) and checkTresxTres
    return validezSudoku


if __name__ == '__main__':
    assert check_sudoku([[1, 2, 3, 4],
                         [2, 3, 1, 3],
                         [3, 1, 2, 3],
                         [4, 4, 4, 2]]) == False
    assert check_sudoku([[1, 2, 3],
                         [2, 3, 1],
                         [3, 1, 2]]) == True
    assert check_sudoku([[1, 2, 3, 4],
                         [2, 3, 4, 1],
                         [3, 4, 1, 2],
                         [4, 1, 2, 3]]) == True
