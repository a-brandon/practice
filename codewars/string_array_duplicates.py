def dup(arry):
    out = []

    for s in arry:
        unique = [s[0]]

        for ch in s[1:]:
            if ch != unique[-1]:
                unique.append(ch)

        out.append(''.join(unique))

    return out