def erase(txt):
    if txt.count('#') == len(txt):
        return ''

    stack = []
    for c in txt:
        if c != '#':
            stack.append(c)
        elif not stack:
            continue
        else:
            stack.pop()
    return ''.join(stack)
