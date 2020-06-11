def expand(num):
    s = str(num)[::-1]
    l = [x + str(i * '0') for i, x in enumerate(s) if x != '0']
    return ' + '.join(l[::-1])