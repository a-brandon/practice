import itertools


def permutations(s):
    return ' '.join(sorted(''.join(p) for p in itertools.permutations(s)))