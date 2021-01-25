import itertools


def combine_lists(*args):
    return [[x, y, z] for x, y, z in itertools.zip_longest(*args, fillvalue='*')]