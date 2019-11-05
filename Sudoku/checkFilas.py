def checkFilas(sudoku):

    # Precondicion
    assert isinstance(sudoku, list)
    for fila in sudoku:

        for (posicion, numero) in enumerate(fila):
            # enumerate devuelve (offset, item): offset es la posicion del item en la lista (fila)
            # y se incrementa automaticamente en 1 en cada iteracion
            # Averiguo si el numero se encuentra en el resto de la fila /lista
            # (siguiente posicion hasta la ultima)
            if numero in fila[posicion + 1:]:
                return False

    return True


### CASOS TEST ###

if __name__ == '__main__':