def get_vowel_substrings(txt):
    subs = []
    vowels = ('a', 'e', 'i', 'o', 'u')

    i = 0
    while i < len(txt):
        for j in range(len(txt)):
            s = txt[0:j + 1]
            if s not in subs and s[0] in vowels and s[-1] in vowels:
                subs.append(s)
        txt = txt[i + 1:]

    return sorted(subs)


def get_consonant_substrings(txt):
    subs = []
    vowels = ('a', 'e', 'i', 'o', 'u')

    i = 0
    while i < len(txt):
        for j in range(len(txt)):
            s = txt[0:j + 1]
            if s not in subs and s[0] not in vowels and s[-1] not in vowels:
                subs.append(s)
        txt = txt[i + 1:]

    return sorted(subs)
