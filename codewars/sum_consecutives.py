def sum_consecutives(s):
    prev, totals = None, []

    for i in s:
        if i == prev:
            totals[-1] += i
        else:
            prev = i
            totals.append(prev)

    return totals