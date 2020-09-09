def hangman(phrase, lst):
    return ''.join('-' if letter.lower() not in lst and letter.isalpha() else letter for letter in phrase)