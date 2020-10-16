from itertools import permutations as perm


def permutations(string):
    return list(set(''.join(p) for p in perm(string)))