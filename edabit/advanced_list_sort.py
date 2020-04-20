def advanced_sort(lst):
    return sorted([[x] * lst.count(x) for x in set(lst)], key=lambda x: lst.index(x[0]))
