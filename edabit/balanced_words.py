def balanced_word(word):
    mid = len(word) // 2
    l, r = word[:mid], word[mid:]
    if len(word) % 2:
        r = word[mid + 1:]

    lc, rc = 0, 0
    i = 0
    while i < len(l):
        lc += ord(l[i]) - 96
        rc += ord(r[i]) - 96
        i += 1

    return lc == rc