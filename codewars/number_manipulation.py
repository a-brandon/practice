def manipulate(n):
    x = list(str(n))
    mid = len(x) // 2
    x[mid:] = '0' * len(x[mid:])
    return int(''.join(x))