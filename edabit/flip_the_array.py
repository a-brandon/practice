def flip_list(lst):
    if lst:
        return [[i] for i in lst if type(lst[0]) == int] or sum(lst, [])
    return []
