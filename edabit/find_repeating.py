def find_repeating(txt):
    if not txt:
        return []

    clusters = []
    values = [txt[0], 0, 0, 1]
    for i, ch in enumerate(txt[1:], start=1):
        if ch == values[0]:
            values[2] += 1
            values[3] += 1
        else:
            clusters.append(values)
            values = [txt[i], i, i, 1]

    return clusters + [values]