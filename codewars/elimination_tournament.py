def tourney(inp):
    output = [inp]

    while len(inp) > 1:
        l = [max(inp[i: i + 2]) for i in range(0, len(inp), 2)]

        if len(inp) % 2:
            l = [l.pop()] + l

        output.append(l)
        inp = l

    return output