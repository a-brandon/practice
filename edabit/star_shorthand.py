def to_star_shorthand(txt):
    chars = sorted(set(txt), key=list(txt).index)
    return ''.join(s + '*' + str(txt.count(s)) if txt.count(s) > 1 else s for s in chars)
