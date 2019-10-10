from equacion_segundo_grado import raizEcuacionSegundoGrado
​
​
def test_raiz_nula_unica():
    assert raizEcuacionSegundoGrado(1, 0, 0) == 0
​
def test_coeficiente_c_nulo():
    x, y = raizEcuacionSegundoGrado(1, 1, 0)
    assert x == 0
    assert y == -1
    x, y = raizEcuacionSegundoGrado(2, 4, 0)
    assert x == 0
    assert y == -2