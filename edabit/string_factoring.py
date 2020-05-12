def string_factor(lst):
    nums = set(lst)
    if len(nums) == 1:
        x = lst[0]
        return '{}^{}'.format(x, lst.count(x))

    digits = sorted(set(nums), key=lst.index)
    build = ['{} x ' if lst.count(x) == 1 else '{}^{} x ' for x in digits]
    output = []
    
    for x, y in zip(digits, build):
        if '^{}' in y:
            y = y.replace('^{}', str(lst.count(x))).replace(y[0:2], str(x) + '^')
            output.append(y)
        else:
            y = y.replace('{}', str(x))
            output.append(y)
            
    return ''.join(output)[:-3]
