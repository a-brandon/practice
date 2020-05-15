def count_same_ends(txt):
    words = ''.join(c.lower() for c in txt if c.isalpha() or c == ' ').split()
    return sum(w[0] == w[-1] for w in words if len(w) > 1)
