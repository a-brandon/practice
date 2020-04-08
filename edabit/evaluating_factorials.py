def eval_factorial(lst):
    f = []
    for fact in lst:
        if fact == '0!' or fact == '1!':
            f.append(1)
            continue
        fact = [i for i in range(1, int(fact[0:-1]) + 1)]
        res = 1
        for x in fact:
            res *= x
        f.append(res)
    return sum(f)
