from itertools import permutations


def permute_a_palindrome(input):
    inputcopy = reverse(input)
    if inputcopy == input:
        return True
    else:
        permuted = ["".join(p) for p in permutations(input)]
        for j in permuted:
            if j == reverse(j):
                return True
        return False


def reverse(input):
    stringreverse = ""
    for i in input:
        stringreverse = i + stringreverse
    return stringreverse


if __name__ == "__main__":
    assert permute_a_palindrome("owo") == True
    assert permute_a_palindrome("hola") == False
    assert permute_a_palindrome("oww") == True
