def no_duplicate_letters(phrase):
    return False if any(w.count(c) > 1 for w in phrase.lower().split() for c in w) else True