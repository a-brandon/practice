def fold_array(array, runs):
    while runs > 0:
        p = len(array) // 2

        if len(array) % 2:
            l, r = array[:p], array[-1:p:-1]
            array = [sum((x, y)) for x, y in zip(l, r)] + [array[p]]
        else:
            array = [sum((x, y)) for x, y in [*zip(array, array[::-1])][:p]]

        runs -= 1

    return array