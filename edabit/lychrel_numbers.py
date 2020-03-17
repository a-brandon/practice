def lychrel(n):
    if str(n) == str(n)[::-1]:
        return 0
    count = 0
    while str(n) != str(n)[::-1]:
        n += int(str(n)[::-1])
        count += 1
        if count >= 500:
            return True
    return count
