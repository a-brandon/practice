def is_word_chain(words):
    for (a, b) in zip(words, words[1:]):
        if len(a) != len(b) or len(set(a) - set(b)) > 1:
            return False
    return True
