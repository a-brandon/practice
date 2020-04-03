def completely_filled(lst):
    if len(lst) == 1 and len(lst[0]) <= 2:
        return True
    counts = [box.count('*') + box.count('#') for box in lst[1:-1]]
    return all(x == lst[0].count('#') for x in counts)
