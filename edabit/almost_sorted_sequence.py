def almost_sorted(lst):
    if lst in [sorted(lst), sorted(lst, reverse=True)]:
        return False

    i = 0
    while i < len(lst):
        x = lst.pop(i)
        if lst == sorted(lst) or lst == sorted(lst, reverse=True):
            return True
        lst.insert(i, x)
        i += 1
    return False
