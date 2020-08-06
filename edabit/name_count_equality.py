def equal_count(txt, names):
    s = names.split('&')
    d = {n: 0 for n in s}

    for k in d:
        d[k] += txt.count(k)

    if d[s[0]] == d[s[1]]:
        d['equality'] = True
    else:
        d['equality'] = False
        d['difference'] = abs(d[s[0]] - d[s[1]])

    return d