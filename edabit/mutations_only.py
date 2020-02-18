def zeroes_to_end(lst):
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(0)
    return lst
