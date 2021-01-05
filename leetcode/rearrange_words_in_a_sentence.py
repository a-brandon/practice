def arrange_words(text):
    words = sorted(text.lower().split(), key=len)
    return ' '.join(words).capitalize()