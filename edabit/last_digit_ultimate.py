def last_dig(a: int, b: int, c: int) -> bool:
    a, b, c = str(a), str(b), str(c)
    result = [int((num[-1])) for num in (a, b, c)]
    product = str(result[0] * result[1])
    return int(product[-1]) == result[2]
