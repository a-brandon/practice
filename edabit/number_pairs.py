def number_pairs(txt):
    s = txt.split()[1:]
    lookup = {x: s.count(x) for x in s}
    pairs = 0

    for v in lookup.values():
        while v > 1:
            v -= 2
            pairs += 1

    return pairs