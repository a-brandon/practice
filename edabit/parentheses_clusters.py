def split(txt):
    if not txt or txt[0] == ')':
        return []

    i, counter = 0, 0
    stack, clusters = [], []
    for paren in txt:
        if paren == '(':
            stack.append(paren)
            counter += 1
        else:
            stack.append(paren)
            counter -= 1
            if counter == 0:
                clusters.append(''.join(stack))
                stack = []

    return clusters
