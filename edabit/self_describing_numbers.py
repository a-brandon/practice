def is_self_describing(num: int) -> bool:
    if len(str(num)) % 2 != 0:
        return False
    num = str(num)
    pairs = [num[i * 2: i * 2 + 2] for i in range(len(num) // 2)]
    return all(len(int(x) * y) == num.count(y) for x, y in pairs)
