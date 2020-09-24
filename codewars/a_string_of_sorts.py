def sort_string(s, ordering):
    unique_order = sorted(set(ordering), key=ordering.index)
    l, r = [], []

    for c in s:
        if c in unique_order:
            l.append(c)
        else:
            r.append(c)

    return ''.join(sorted(l, key=unique_order.index) + r)