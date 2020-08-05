def staircase(n):
    x = -n if n < 0 else n
    l = []
    for i in range(x):
        l.append(('_' * (x - 1)) + ('#' * (i + 1)))
        x -= 1
    return '\n'.join(l) if n >= 1 else '\n'.join(l[::-1])