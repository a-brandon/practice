def pseudo_sort(st):
    words = ''.join(c for c in st if c.isalpha() or c.isspace()).split()
    lower, upper = [], []

    for w in words:
        if w[0].isupper():
            upper.append(w)
        else:
            lower.append(w)

    return ' '.join(sorted(lower) + sorted(upper, reverse=True))