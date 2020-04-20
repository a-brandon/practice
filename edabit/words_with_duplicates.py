def no_duplicate_letters(phrase):
    case = phrase.lower().split()
    return not any(word != ''.join(sorted(set(word), key=lambda x: word.index(x))) for word in case)
