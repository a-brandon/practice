def is_checkerboard(lst):
    for elem in zip(*lst):
        for i, _ in enumerate(elem[:-1]):
            if elem[i] == elem[i + 1]:
                return False
    return True
