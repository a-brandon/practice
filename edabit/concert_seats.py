def can_see_stage(seats):
    counter = 0
    for el in zip(*seats[::-1]):
        if all(el[i] > el[i + 1] for i, _ in enumerate(el[:-1])):
            counter += 1
    return counter == len(seats[0])
