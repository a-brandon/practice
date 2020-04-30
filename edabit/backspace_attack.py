def erase(txt):
    stack = []
    for c in txt:
        if c != '#':
            stack.append(c)
        elif not stack:
            continue
        else:
            stack.pop()
    return ''.join(stack)
