def permute_a_palindrome(input):
    input = input.lower()
    inputcopy = reverse(input)
    if inputcopy == input:
        return True
    else:
        return comparacion_input(input)


def comparacion_input(input):
    countImpar = 0
    input = input.lower()
    for char in input:
        number = input.count(char)
        if number % 2 != 0:
            countImpar = countImpar + 1
    if countImpar == 1:
        return True
    else:
        return False


def reverse(input):
    input = input.lower()
    stringreverse = ""
    for i in input:
        stringreverse = i + stringreverse
    return stringreverse


if __name__ == "__main__":
    assert permute_a_palindrome("owo") == True
    assert permute_a_palindrome("hola") == False
    assert permute_a_palindrome("oww") == True
    assert permute_a_palindrome("Ooww") == True
    assert permute_a_palindrome("ooow") == False
