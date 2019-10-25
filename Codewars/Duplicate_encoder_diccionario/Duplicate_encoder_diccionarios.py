def duplicate_encoder_diccionarios(input):
    diccionario = {}
    for caracter in input:
        caracter = caracter.lower()
        if caracter in diccionario:
            diccionario[caracter] = ")"
        else:
            diccionario[caracter] = "("
    assert diccionario != {}
    string = ""
    for caracter in input:
        string = string + diccionario[caracter]
    return string


print(duplicate_encoder_diccionarios("hola"))