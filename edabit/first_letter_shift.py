def shift_sentence(txt):
    s = txt.split()
    for i, w in enumerate(s):
        if w == s[0]:
            s[i] = s[-1][0] + w[1:]
        else:
            s[i] = txt.split()[i - 1][0] + w[1:]
    return ' '.join(s)