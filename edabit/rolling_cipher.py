from string import ascii_lowercase


def rolling_cipher(txt, n):
    alpha = ascii_lowercase + ascii_lowercase
    return ''.join(alpha[alpha.index(c) + n] for c in txt)
