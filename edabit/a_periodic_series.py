def periodic(n):
    terms, c = {n}, 0
    while True:
        x = len(n)
        n += str(sum(map(int, list(n))))
        n = n[-x:]
        if n in terms:
            return c + 1
        terms.add(n)
        c += 1
