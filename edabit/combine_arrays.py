import itertools


def combine_lists(lst1, lst2, lst3):
    return [[x, y, z] for x, y, z in itertools.zip_longest(lst1, lst2, lst3, fillvalue='*')]