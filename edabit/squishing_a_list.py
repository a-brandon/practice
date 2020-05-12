def squish(lst, d):
    if not lst:
        return []
    elif d == 'right' and lst:
        return [lst[0: i] + [sum(lst[i:])] for i in range(len(lst), -1, -1)][1:]
    return [lst] + [[sum(lst[0: i + 2])] + lst[i + 2:] for i in range(0, len(lst), 1)][0:-1]
