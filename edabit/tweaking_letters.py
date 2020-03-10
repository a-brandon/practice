from string import ascii_lowercase

def tweak_letters(txt, lst):
    alpha = ascii_lowercase
    print(alpha)
    tweaked = ''
    for i, ch in enumerate(txt):
        if ch == 'z':
            tweaked += 'a'
        else:
            tweaked += alpha[alpha.index(ch) + lst[i]]
    return tweaked
