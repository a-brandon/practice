def longest_repetition(chars):
    if not chars:
        return ('', 0)

    stack, reps = [chars[0]], []

    for c in chars[1:]:
        if c != stack[-1]:
            reps.append((stack[0], len(stack)))
            stack = [c]
        else:
            stack.append(c)
    reps.append((stack[0], len(stack)))

    return max(reps, key=lambda t: t[1])