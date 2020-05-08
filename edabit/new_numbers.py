from itertools import permutations as perm


def is_new(n):
    nums = [int(''.join(x)) for x in perm(str(n))]
    return not any(x < n and sorted(str(x)) == sorted((str(n))) for x in nums)
