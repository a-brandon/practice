def replace_nth(txt, nth, old_char, new_char):
    if nth <= 0 or nth > txt.count(old_char):
        return txt

    old_chars = [i for i, ch in enumerate(txt) if ch == old_char]
    letters = list(txt)
    for i in old_chars[nth - 1::nth]:
        letters[i] = new_char
    return ''.join(letters)
