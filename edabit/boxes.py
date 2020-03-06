def box_seq(step):
    box = 0
    cycle = 0
    while cycle < step:
        box += 3
        cycle += 1
        if cycle == step:
            break
        box -= 1
        cycle += 1
        if cycle == step:
            break
    return box
