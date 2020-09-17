def junction_or_self(n):
    arr = []

    for i in range(1, n):
        s = sum(int(x) for x in str(i))
        if i + s == n:
            arr.append(i)

    return sorted(arr, reverse=True) or 'Self'