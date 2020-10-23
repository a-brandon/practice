def dig_pow(n, p):
    nums, total = list(str(n)), 0
    k = 1

    for i in nums:
        total += int(i) ** p
        p += 1

    while True:
        prod = k * n
        if prod == total:
            return k
        elif prod > total:
            return -1
        k += 1