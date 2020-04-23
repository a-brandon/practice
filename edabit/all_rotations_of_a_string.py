def left_rotations(txt):
    return [txt[i:] + txt[:i] for i in range(len(txt))]


def right_rotations(txt):
    return [txt[-i:] + txt[:-i] for i in range(len(txt))]
