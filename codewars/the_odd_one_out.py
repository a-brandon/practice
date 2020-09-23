def odd_one_out(s):
    lookup = {}

    for ch in s:
        if ch not in lookup:
            lookup[ch] = 1
        else:
            lookup[ch] += 1

    return sorted((c for c in lookup.keys() if lookup[c] % 2), key=s.rindex)