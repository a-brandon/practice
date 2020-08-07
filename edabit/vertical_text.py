def vertical_txt(txt):
    words = txt.split()
    longest_word = max(txt.split(), key=len)

    for i, w in enumerate(words):
        if len(w) != len(longest_word):
            words[i] = w + (' ' * (len(longest_word) - len(w)))

    return [*map(list, zip(*words))]