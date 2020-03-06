def advanced_sort(lst):
    dupes = [[x] * lst.count(x) for x in lst]
    unique = []
    for el in dupes:
        if el not in unique:
            unique.append(el)
    return unique
