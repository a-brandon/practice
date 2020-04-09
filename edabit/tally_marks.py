def get_normal(lst):
    res = []
    for x in lst:
        if '5' not in str(x):
            res.append(x)
        else:
            fives = str(x).count('5') * 5
            rem_nums = sum(int(n) for n in str(x) if n != '5')
            res.append(fives + rem_nums)
    return res


def get_tally(lst):
    res = []
    for x in lst:
        if x >= 5 and not x % 5:
            res.append(int('5' * (x // 5)))
        elif x >= 5:
            floor, rem = x // 5, x % 5
            res.append(int('5' * floor + str(rem)))
        else:
            res.append(x)
    return res


def switch_notation(scores, desired_notation):
    if desired_notation == 'normal':
        return get_normal(scores)
    return get_tally(scores)
