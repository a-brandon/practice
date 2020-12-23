def shifted_diff(first, second):
    if set(first) != set(second):
        return -1

    n = 0
    first_letters = list(first)

    while ''.join(first_letters) != second:
        first_letters.insert(0, first_letters.pop())
        n += 1

        if ''.join(first_letters) == first:
            return -1

    return n