def uncensor(txt, vowels):
    v = list(vowels)[::-1]
    return ''.join(v.pop() if c == '*' else c for c in txt)