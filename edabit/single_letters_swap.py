def validate_swaps(lst, txt):
    swaps = []
    for word in lst:
        if len(word) > len(txt) or set(word) != set(txt):
            swaps.append(False)
            continue
        counter, letters = 0, list(word)
        for i, c in enumerate(word[:]):
            if c != txt[i]:
                c_idx = txt.index(c)
                letters[c_idx] = txt[c_idx]
                counter += 1
        swaps.append(True if counter == 2 else False)
    return swaps
