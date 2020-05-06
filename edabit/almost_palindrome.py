def almost_palindrome(txt):
    return sum(a != b for a, b in zip(txt, txt[1:][::-1][:-1])) == 1
