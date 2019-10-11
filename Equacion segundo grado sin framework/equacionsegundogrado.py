
from math import sqrt


def raizEcuacionSegundoGrado(a, b, c):

    if b == c == 0:
        return 0

    if c == 0:
        x = 0
        y = -b / a
        return x, y

    if b == 0:
        x = sqrt(-c/a)
        y = -sqrt(-c/a)
        return x, y

    if a == 0:
        x = None
        y = None
        return x, y

    radicando = b**2 - 4*a*c
   
    if radicando >= 0:
        x = (-b + sqrt(radicando)) / (2 * a)
        y = (-b - sqrt(radicando)) / (2 * a)
        return x, y
    else:
        x = None
        y = None
        return x, y        


if __name__ == "__main__":
    x, y = raizEcuacionSegundoGrado(1, 1, 0)
    assert x == 0
    assert y == -1
    x, y = raizEcuacionSegundoGrado(2, 4, 0)
    assert x == 0
    assert y == -2 
    x, y = raizEcuacionSegundoGrado(1, 0, -1)
    assert x == 1
    assert y == -1
    x, y = raizEcuacionSegundoGrado(0, 20, 5)
    assert x == None
    assert y == None
    x, y = raizEcuacionSegundoGrado(5, -20, 15)
    assert x == 3
    assert y == 1
