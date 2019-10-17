def duplicate_encode(word):
    word = word.lower()
    lengthWord = len(word)
    initial = -1
    actualLengthWord = 0
    codedString = ""
    while lengthWord > actualLengthWord:
        initial = initial + 1
        letter = word[initial]
        counted = word.count(letter)
        if counted == 1:
            coded = "("
        else:
            coded = ")"
        actualLengthWord = actualLengthWord + 1
        codedString = codedString + coded
    return codedString


if __name__ == "__main__":
    codedString = duplicate_encode("hola")
    assert codedString == "(((("
    codedString = duplicate_encode("hhhh")
    assert codedString == "))))"
    codedString = duplicate_encode("HuLl")
    assert codedString == "(())"
