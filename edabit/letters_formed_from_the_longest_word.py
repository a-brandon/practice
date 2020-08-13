def can_form(lst):
    words = sorted(lst, key=len)

    for w in words[:-1]:
        for c in words[-1]:
            w = w.replace(c, '', 1)
        if w:
            return False

    return True