from string import ascii_lowercase


def message_glitch(txt):
    indices = ''.join(d if d.isdigit() else ' ' for d in txt).split()
    indices = list(map(int, indices))
    for i in indices:
        txt = txt.replace(str(i), ascii_lowercase[i - 1], 1)
    return txt
