def group(arr: list) -> list:
    arr = [[x] * arr.count(x) for x in arr]
    res = []
    for x in arr:
        if x not in res:
            res.append(x)
    return res
