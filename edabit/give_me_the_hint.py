def grant_the_hint(txt):
    txt = txt.split()
    hints = [' '.join('_' * len(word) for word in txt)]
    iterations = max(len(word) for word in txt)
    for i in range(iterations):
        reveals = [' '.join(word[0:i + 1] + ('_' * (len(word) - (i + 1))) for word in txt)]
        hints.extend(reveals)
    return hints
