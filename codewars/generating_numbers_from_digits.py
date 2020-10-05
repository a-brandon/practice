from itertools import permutations as perm


def proc_arr(arr):
    perms = set(int(''.join(p)) for p in perm(arr))
    return [len(perms), min(perms), max(perms)]