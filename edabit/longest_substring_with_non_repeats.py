def longest_nonrepeating_substring(txt):
    if len(set(txt)) == 1:
        return txt[0]
    if len(set(txt)) == len(txt):
        return txt

    subs = []
    for i, c in enumerate(txt):
        j = 0
        while j < len(txt):
            comp = txt[i:j + 3]
            if len(set(comp)) == len(comp):
                subs.append(comp)
            j += 1
    return max(subs, key=len)
