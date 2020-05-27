def lychrel(n):
    count = 0
    while str(n) != str(n)[::-1] and count < 500:
        n = n + int(str(n)[::-1])
        count += 1
    return count if count < 500 else True
