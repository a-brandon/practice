def absolute(txt):
    words = txt.split()

    for i, w in enumerate(words):
        if w == 'A':
            words[i] = 'An absolute'
        elif w == 'a':
            words[i] = 'an absolute'

    return ' '.join(words)