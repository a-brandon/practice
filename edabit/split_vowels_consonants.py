def split(txt):
    vowels = [character for character in txt if character in ['a', 'e', 'i', 'o', 'u']]
    remaining_chars = [character for character in txt if character not in ['a', 'e', 'i', 'o', 'u']]
    return ''.join(vowels + remaining_chars)
