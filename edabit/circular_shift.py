def circular_shift(l1, l2, n):
    if l1 == l2:
        return True
    res = []
    for _, num in enumerate(l1):
        comb_lists = l1 + l1
        two_idx = comb_lists[(l1 + l1).index(num) + n]
        res.append(two_idx)
    return res == l2
