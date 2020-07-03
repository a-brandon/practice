def get_factors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


def factor_sort(nums):
    factor_map = {n: get_factors(n) for n in nums}
    vals = sorted(set(factor_map.values()), reverse=True)
    res, l = [], sorted(nums, reverse=True)

    i = 0
    while i < len(vals):
        for x in l:
            if factor_map.get(x) == vals[i]:
                res.append(x)
        i += 1

    return res