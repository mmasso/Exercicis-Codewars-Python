from checkCuadrado import checkCuadrado
from checkNumero import checkNumerosValidos
from checkFilas import checkFilas
from checkColumnas import checkColumnas


def check_sudoku(sudoku):
    validezSudoku = checkCuadrado(sudoku) and checkNumero(sudoku) \
        and checkFilas(sudoku) and checkColumnas(sudoku)
    return validezSudoku


if __name__ == '__main__':