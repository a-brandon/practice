def is_self_describing(num):
    if len(str(num)) % 2 != 0:
        return False

    x = str(num)
    return all(int(x[i * 2: i * 2 + 2][0]) == x.count(x[i * 2: i * 2 + 2][1]) for i in range(len(x) // 2))
