def reverse_lego_yoda(text):
    t = text.split('.')
    s = ''

    for w in t[:-1]:
        w = w.strip().replace(',', '.')
        p = w.index('.')
        sentence = w[p + 2:] + ' ' + w[:p] + '. '
        s += sentence[0].upper() + ''.join(map(str.lower, sentence[1:]))

    return s.replace('area', 'Area')