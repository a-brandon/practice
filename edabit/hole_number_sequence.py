def sum_of_holes(n):
    d = {0: 1, 4: 1, 6: 1, 8: 2, 9: 1}
    c = 0
    for i in range(1, n + 1):
        if len(str(i)) == 1:
            c += d.get(i, 0)
        else:
            c += sum(d.get(int(x), 0) for x in str(i))
    return c