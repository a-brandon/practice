def zeroes_to_end(lst):
    if lst.count(0) == len(lst) or lst.count(0) == 0:
        return lst
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst
