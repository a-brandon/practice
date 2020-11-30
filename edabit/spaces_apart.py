def space_apart(lst):
    x = lst.count('1')
    if x < 2 or x > 2:
        return 'invalid'

    start, end = [i for i, x in enumerate(lst) if x == '1']
    counter = 0

    for i in lst[start + 1:end]:
        if isinstance(i, int):
            if i >= 0:
                counter += i
            else:
                return 'invalid'

    return counter