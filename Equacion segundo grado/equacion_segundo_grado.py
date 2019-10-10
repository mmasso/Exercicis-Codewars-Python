def raizEcuacionSegundoGrado(a, b, c):
    
    if b == c == 0:
        return 0
    
    if c == 0:
        x = 0
        y = -b / a
        return x, y 