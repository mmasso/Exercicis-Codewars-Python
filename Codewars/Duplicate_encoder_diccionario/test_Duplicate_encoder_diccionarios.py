from Duplicate_encoder_diccionarios import duplicate_encoder_diccionarios​


def test_todos_caracteres_diferentes():
    assert duplicate_encoder_diccionarios("hola") == "(((("
