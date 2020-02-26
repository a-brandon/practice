def right_side(arr):
    r_side = []
    while arr:
        n = arr[0]
        counts = sum(1 for x in arr if x < n)
        r_side.append(counts)
        arr.pop(0)
    return r_side


def left_side(arr):
    l_side = []
    while arr:
        n = arr[-1]
        counts = sum(1 for x in arr if x < n)
        l_side.append(counts)
        arr.pop(-1)
    return l_side[::-1]
