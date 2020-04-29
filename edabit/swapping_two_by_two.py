def swap_two(txt):
    quads = []
    for i in range(len(txt)):
        group = txt[i * 4: i * 4 + 4]
        if group:
            quads.append(group)
    return ''.join(x[-2:] + x[0:-2] if len(x) == 4 else x for x in quads)
