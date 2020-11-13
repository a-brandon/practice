def solve(arr):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    totals = []
    for w in arr:
        t = 0

        for c in w:
            t += alpha.index(c.lower()) == w.index(c)
            w = w.replace(c, '_', 1)

        totals.append(t)

    return totals