def pairs(lst):
    if len(lst) % 2 != 0:
        mid = len(lst) // 2
        last_el = [[lst.pop(mid)] * 2]
        return [[a, b] for a, b in zip(lst, lst[::-1][:mid])] + last_el
    return [[a, b] for a, b in zip(lst, lst[::-1][:len(lst) // 2])] or []
