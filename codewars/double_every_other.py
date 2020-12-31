def double_every_other(lst):
    lst[1::2] = map(lambda i: i * 2, lst[1::2])
    return lst