def shuffle_count(num):
    arr = [*range(1, num + 1)]
    p = len(arr) // 2
    f, s = arr[0:p], arr[p:]
    i, c = 1, 0

    while True:
        for x in s:
            f.insert(i, x)
            i += 2
        i = 1

        f, s = f[0:p], f[p:]

        c += 1
        if f + s == arr:
            return c