def letters(word1, word2):
    l = [[set(word1) & set(word2)], [set(word1) - set(word2)], [set(word2) - set(word1)]]
    res = [''.join(sorted(el[0])) for el in l]
    return res