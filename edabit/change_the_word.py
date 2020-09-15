def change_string(word):
    alpha = 'abcdefghijklmnopqrstuvwxyz' * 2
    l = list(word[::-1])

    for i, ch in enumerate(l):
        if ch.islower():
            l[i] = ch.upper()
        else:
            l[i] = alpha[alpha.index(ch.lower()) + 1].upper()

    return ''.join(l)