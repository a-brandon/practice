from itertools import zip_longest


def carry_digits(n1, n2):
    n1, n2 = str(n1), str(n2)
    totals = [int(x) + int(y) for x, y in zip_longest(n1[::-1], n2[::-1], fillvalue=0)] + [0]
    carries = 0
    for i, n in enumerate(totals):
        if n >= 10:
            totals[i + 1] += 1
            carries += 1
    return carries