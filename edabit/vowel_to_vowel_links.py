def vowel_links(txt):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return any(w[-1] in vowels and txt.split()[i + 1][0] in vowels for i, w in enumerate(txt.split()[:-1]))