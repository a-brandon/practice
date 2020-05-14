def convert_base(num, base):
    res = []
    while num > 0:
        rem = num % base
        res.append(str(rem))
        num //= base
    return list(map(int, res))[::-1]


def esthetic(num):
    x = num
    bases = []
    base = 10

    while base > 1:
        curr_base = convert_base(num, base)
        if all(abs(curr_base[i] - curr_base[i + 1]) == 1 for i, _ in enumerate(curr_base[:-1])):
            bases.append(base)
            base -= 1
            num = x
        else:
            base -= 1
            num = x

    return bases[::-1] or 'Anti-Esthetic'
