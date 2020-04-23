def can_build(txt1, txt2):
    letters, letters_two = txt1.replace(' ', ''), txt2.replace(' ', '')
    for c in letters_two:
        if c in letters:
            letters = letters.replace(c, '_', 1)
        if letters == '_' * len(letters):
            return True
    return False
