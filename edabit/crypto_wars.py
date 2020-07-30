def decrypt(lst):
    l = sorted(lst)
    r = range(l[0], l[-1] + 1)
    return chr(96 + list(set(r) - set(l))[0]).upper()