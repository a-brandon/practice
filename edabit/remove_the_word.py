def remove_letters(letters, word):
    letters = ''.join(letters)
    for c in word:
        letters = letters.replace(c, '', 1)
    return list(letters)
