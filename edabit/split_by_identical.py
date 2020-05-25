def split_groups(txt):
    s, clusters = txt[0], []

    for c in txt[1:]:
        if c != s[-1]:
            clusters.append(s)
            s = ''
        s += c

    return clusters + [s]
