def checkTresxTres(sudoku):
    assert isinstance(sudoku, list)
    if len(sudoku) == 9:
        tresXtres = []
        contador = 0     
        for fila in sudoku:
            if fila not in tresXtres:
                tresXtres.append(fila[0:3])
                contador = contador + 1
                if contador == 3:
                    break
        valors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for fila in tresXtres:
            for value in fila:
                if value not in valors:
                    return False
                valors.remove(value)
        return True
    return True


if __name__ == "__main__":
    assert checkTresxTres([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                           [6, 7, 2, 1, 9, 5, 3, 4, 8],
                           [1, 9, 8, 3, 4, 2, 5, 6, 7],
                           [8, 5, 9, 7, 6, 1, 4, 2, 3],
                           [4, 2, 6, 8, 5, 3, 7, 9, 1],
                           [7, 1, 3, 9, 2, 4, 8, 5, 6],
                           [9, 6, 1, 5, 3, 7, 2, 8, 4],
                           [2, 8, 7, 4, 1, 9, 6, 3, 5],
                           [3, 4, 5, 2, 8, 6, 1, 7, 9]]) == True
