def special_reverse_string(txt):
    l = list(txt.replace(' ', ''))
    r = ''
    for c in txt:
        if c.isspace():
            r += ' '
        else:
            r += l.pop().upper() if c.isupper() else l.pop().lower()
    return r
