def multiply(nums) -> int:
    res = 1
    for x in nums:
        res *= x
    return res


def eval_factorial(lst):
    f = []
    for fact in lst:
        if fact == '0!' or fact == '1!':
            f.append(1)
            continue
        fact = multiply(i for i in range(1, int(fact[0:-1]) + 1))
        f.append(fact)
    return sum(f)
