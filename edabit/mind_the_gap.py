def is_gapful(n):
    return True if n % int(str(n)[0] + str(n)[-1]) == 0 and len(str(n)) >= 3 else False


def gapful(n):
    x, l, h = str(n), n, n
    if len(x) == 2:
        return 100

    while True:
        if is_gapful(l) and is_gapful(h):
            closest_num = l if abs(n - l) < abs(n - h) else h
            return closest_num
        elif is_gapful(l):
            return l
        elif is_gapful(h):
            return h
        l += 1
        h -= 1
