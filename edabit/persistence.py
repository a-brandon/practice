def additive_persistence(n):
    counter = 0
    while len(str(n)) > 1:
        n = sum(map(int, list(str(n))))
        counter += 1
    return counter


def multiplicative_persistence(n):
    counter = 0
    while len(str(n)) > 1:
        prod = 1
        for x in str(n):
            prod *= int(x)
        counter += 1
        n = prod
    return counter