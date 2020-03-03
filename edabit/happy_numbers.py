def happy(n):
    while n > 1:
        n = sum([int(i) ** 2 for i in list(str(n))])
        if n == 4:
            return False
    return True

