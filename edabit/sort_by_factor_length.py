def factor_sort(nums):
    factor_lengths = {}
    for x in nums:
        factors = [i for i in range(1, x + 1) if x % i == 0]
        factor_lengths[x] = len(factors)
    dupes = sorted([k for k, v in factor_lengths.items() if v == 2], reverse=True)
    largest = sorted([k for k, v in factor_lengths.items() if v > 2], reverse=True)
    if dupes[-1] == min(factor_lengths, key=factor_lengths.get):
        dupes.pop(-1)
    return largest + dupes + [min(factor_lengths, key=factor_lengths.get)]
