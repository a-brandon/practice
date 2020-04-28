from string import ascii_lowercase


def tweak_letters(txt, lst):
    alpha = ascii_lowercase * 2
    shift = [alpha[alpha.index(a) + b] for a, b in zip(txt, lst)]
    return ''.join(shift)
