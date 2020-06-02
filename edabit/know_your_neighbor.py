def plus_sign(txt):
    if txt[0].isalpha():
        return False
    letters = [i for i, c in enumerate(txt) if c.isalpha()]
    for i in letters:
        if txt[i - 1] != '+' or txt[i + 1] != '+':
            return False
    return True
