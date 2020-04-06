def split(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = ''
    for c in word:
        if c not in vowels:
            s += '.' + c + '.'
        else:
            s += c
    return ' '.join(s.split('.')).split()
