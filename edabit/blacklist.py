def prevent_distractions(txt):
    for word in ['anime', 'memes', 'vine', 'roasts', 'Danny DeVito']:
        if word in txt:
            return "NO!"
    return "Safe watching!"
