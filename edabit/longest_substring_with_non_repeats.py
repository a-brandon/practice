def longest_nonrepeating_substring(txt):
    if len(set(txt)) == 1:
        return txt[0]
    if len(set(txt)) == len(txt):
        return txt

    subs = []
    for i, _ in enumerate(txt):
        for j in range(len(txt)):
            comp = txt[i:j + 1]
            if len(set(comp)) == len(comp):
                subs.append(comp)
    return max(subs, key=len)
