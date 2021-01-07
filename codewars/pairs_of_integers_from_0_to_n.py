def generate_pairs(n):
    l = []
    x, y = [0, 0]

    while [x, y] != [n, n]:
        l.append([x, y])
        y += 1
        if y == n:
            l.append([x, y])
            x += 1
            y = x

    l.append([x, y])
    return l