# Golf
def larger_than_right(lst):
    return [n for i, n in enumerate(lst[:-1]) if all(n > x for x in lst[i + 1:])] + [lst[-1]] or [lst[0]]
