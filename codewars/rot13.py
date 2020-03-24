from string import ascii_lowercase


def rot13(message):
    alpha = ascii_lowercase + ascii_lowercase
    rot = ''
    for c in message:
        if c.isalpha() and c.isupper():
            idx = alpha.index(c.lower())
            rot += alpha[idx + 13].upper()
        elif c.isalpha() and c.islower():
            idx = alpha.index(c)
            rot += alpha[idx + 13]
        else:
            rot += c
    return rot
