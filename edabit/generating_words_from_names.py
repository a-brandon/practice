def anagram(name, words):
    word_bank = [c.lower() for c in name if c.isalpha()]
    letters = list(''.join(words))
    for c in letters:
        if c not in word_bank:
            return False
        word_bank.remove(c)
    return False if word_bank else True
