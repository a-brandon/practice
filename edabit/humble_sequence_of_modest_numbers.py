def is_modest(num):
    n, count = str(num), 0
    for i in range(len(n[:-1])):
        l, r = int(n[:i + 1]), int(n[i + 1:])
        if r != 0:
            count += 1 if num % r == l else 0
    return count >= 1