from itertools import zip_longest


def zipper(l1, l2):
    if l1 == l2:
        return True
    elif l1[-1] != l2[-1]:
        return False
    
    counter = 0
    for x, y in zip_longest(l1[::-1], l2[::-1], fillvalue=0):
        if x == y:
            counter += 1
    return [len(l1) - (counter + 1), len(l2) - (counter + 1)]
