def permute_a_palindrome(input):
    input = input.lower()
    inputcopy = reverse(input)
    if inputcopy == input:
        return True
    else:
        return comparacion_input(input)

#crear un for on dugui un contador per a cada lletra del input
#el codi que jo he creat serveix per a paraules que tenguin nomes una lletra diferent

def comparacion_input(input):
    input = input.lower()
    contador = 0
    for b in input:
        a = input.count(b)
        if a % 2 != 0:
            contador = contador + 1
    if contador % 2 != 0:
        return True
    else:
        return False
    return True


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
