def simplify(number):
    n = list(str(number))
    res = ''

    for i, x in enumerate(n[:-1]):
        if int(x) > 0:
            zero_count = len(n[i + 1:])
            res += '{}*1{}+'.format(x, '0' * zero_count)

    return res[:-1] if int(n[-1]) == 0 else res + n[-1]