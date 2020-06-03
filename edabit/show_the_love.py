def show_the_love(lst):
    min_num = min(lst)
    lst[lst.index(min_num)] = '_'
    for i, n in enumerate(lst):
        if isinstance(n, int):
            min_num += 0.25 * n
            lst[i] = n - n * 0.25
    lst[lst.index('_')] = min_num
    return lst
