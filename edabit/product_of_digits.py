def sum_dig_prod(*args):
    total = str(sum(args))
    while len(total) > 1:
        x = 1
        for n in total:
            x *= int(n)
        total = str(x)
    return int(total)
