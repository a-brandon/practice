def remove_last_vowel(txt):
    words = txt.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i, word in enumerate(words):
        vowel = max(word.rindex(v) for v in word if v.lower() in vowels or v.upper() in vowels)
        word = list(word)
        word[vowel] = ''
        words[i] = ''.join(word)
    return ' '.join(words)
