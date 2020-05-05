def is_circular(lst):
    l = [lst[0]]
    i = 0

    while i < len(lst[1:]):
        for el in lst[1:]:
            if el[0] == l[-1][-1]:
                l.append(el)
            if len(l) == len(lst):
                i = len(lst[1:])
        i += 1

    if l[-1][-1] == l[0][0]:
        return all(l[i][-1] == l[i + 1][0] for i, _ in enumerate(l[:-1]))
    return False
