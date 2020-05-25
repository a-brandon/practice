def dead_end(n):
    terms = []

    while True:
        s = sum(int(x) for x in str(n))
        if s == 1:
            return len(terms) + 1, 1
        elif n % s == 0:
            n //= s
        else:
            n *= s
        terms.append(n)
        if terms.count(n) == 2: return len(terms), terms[-2]
