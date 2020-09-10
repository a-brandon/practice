def validate_swaps(lst, txt):
    bools = []

    for w in lst:
        swaps = []

        for i, c in enumerate(w):
            if c not in txt or len(w) != len(txt):
                break
            if w[i] != txt[i]:
                swaps.append(c)

        bools.append(True if len(swaps) == 2 else False)

    return bools