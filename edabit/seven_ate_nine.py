def nom_nom(lst):
    while len(lst) > 1:
        if lst[0] > lst[1]:
            lst = [sum([lst[0], lst[1]])] + lst[2:]
        else:
            return lst
    return lst
