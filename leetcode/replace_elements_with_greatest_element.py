def replace_elements(arr):
    res = []
    for i, n in enumerate(arr):
        rem = arr[i + 1:]
        if rem:
            res.append(max(rem))
        else:
            res.append(-1)
    return res