def true_alphabetic(txt):
    t = sorted(txt.replace(' ', ''))[::-1]
    return ''.join(t.pop() if c.isalpha() else ' ' for c in txt)
