def dig_pow(n, p):
    count = len(str(n))
    res = []
    while count > 0:
        for num in str(n):
            res.append(int(num) ** p)
            p += 1
            count -= 1
    res = sum(res)
    return res // n if res % n == 0 else - 1
