def block(lst):
    blocks = 0
    for col in zip(*lst[::-1]):
        if 2 in col:
            blocks += len(col[:col.index(2)])
    return blocks
