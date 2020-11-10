def unique_in_order(iterable):
    prev, l = None, []

    for c in iterable:
        if c != prev:
            l.append(c)
        prev = c

    return l