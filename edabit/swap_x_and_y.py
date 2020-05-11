def swap_xy(txt):
    x, y = txt.replace('(', '').split(')')[0:-1]
    y = str(tuple(int(n) for n in y[2:].split(', ')[::-1]))
    x = str(tuple(int(n) for n in x.split(', ')[::-1]))
    return x + ', ' + y
