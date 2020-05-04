def can_build(lst):
    count = 0
    for a, b in zip(lst, lst[1:]):
        if a[0:] + b[-1] == b or b[0] + a == b:
            count += 1
    return count == len(lst) - 1
