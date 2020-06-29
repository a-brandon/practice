def convert_date(date):
    subs = set(' -./,')
    months = ['January', 'February', 'March',
              'April', 'May', 'June',
              'July', 'August', 'September',
              'October', 'November', 'December']
    months_abbr = ['Jan', 'Feb', 'Mar', 'Apr',
                   'May', 'Jun', 'Jul', 'Aug',
                   'Sep', 'Oct', 'Nov', 'Dec']

    s, l = '', []
    for ch in date:
        if ch in subs:
            l.append(s)
            s = ''
        else:
            s += ch
    l.append(s)

    d = [s for s in l if s]
    output = []
    for c in d:
        m = months_abbr if c in months_abbr else months
        if not c.isdigit():
            output.append(m.index(c) + 1)
        else:
            output.append(int(c))

    return output