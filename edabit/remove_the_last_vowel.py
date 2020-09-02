def remove_last_vowel(txt):
    t = txt.split()

    for i, w in enumerate(t):
        vowel_idx = max(w.rindex(c) for c in set(w) if c.lower() in 'aeiou')
        w = list(w)
        w[vowel_idx] = ''
        t[i] = ''.join(w)

    return ' '.join(t)