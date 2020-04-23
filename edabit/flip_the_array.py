def flip_list(lst):
    return [[i] for i in lst if isinstance(lst[0], int)] or sum(lst, []) or []
