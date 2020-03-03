def merge_arrays(a, b):
    alt = []
    for x, y in zip(a, b):
        alt.append(x)
        alt.append(y)
    rem = [x for x in a + b if x not in alt]
    return alt + rem
