def count_datatypes(*args):
    types = {int: 0, str: 0, bool: 0, list: 0, tuple: 0, dict: 0}
    if args:
        for el in args:
            types[type(el)] += 1
    res = list(types.values())
    return res or [0] * 6
