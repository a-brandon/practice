# Sequence: [5, -10, 3, 50, 100, -20, 11]
# Solution #1


def minmax(data: list) -> tuple:
    """R-1.3

    Write a short Python function, minmax(data),
    that takes a sequence of one or more numbers,
    and returns the smallest and largest numbers,
    in the form of a tuple of length two. Do not use
    the built-in functions min or max in implementing
    your solution."""
    min_num = data[0]
    max_num = data[0]
    for x in data:
        if x < min_num:
            min_num = x
        elif x > max_num:
            max_num = x
    return min_num, max_num


# Solution #2


def minmax_two(data: list) -> tuple:
    """R-1.3

    Write a short Python function, minmax(data),
    that takes a sequence of one or more numbers,
    and returns the smallest and largest numbers,
    in the form of a tuple of length two. Do not use
    the built-in functions min or max in implementing
    your solution."""
    min_num = sorted(data)[0]
    max_num = sorted(data)[-1]
    return min_num, max_num

