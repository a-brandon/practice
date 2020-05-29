def encrypt(word):
    vowels = ('a', 'e', 'o', 'u')
    return ''.join(str(vowels.index(c)) if c in vowels else c for c in word[::-1]) + 'aca'
