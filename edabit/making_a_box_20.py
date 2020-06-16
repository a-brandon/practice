def char_box(size):
    if size == 0:
        return [[]]
    elif not isinstance(size, int) or size < 0:
        return - 1

    matrix = []
    for i in range(size):
        if i == 0 or i == size - 1:
            matrix.append(list('#' * size))
        else:
            matrix.append(list('#' + (' ' * (size - 2)) + '#'))
    return matrix