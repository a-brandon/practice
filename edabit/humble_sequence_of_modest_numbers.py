def is_modest(num):
    n, count = str(num), 0

    for i in range(len(n[:-1])):
        l, r = int(n[:i + 1]), int(n[i + 1:])
        if r != 0 and num % r == l:
            count += 1

    return count >= 1