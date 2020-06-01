def first_repeat(chars):
    letters = [chars[0]]
    for c in chars[1:]:
        if c in letters:
            return c
        letters.append(c)
    return '-1'
