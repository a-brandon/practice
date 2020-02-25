def does_rhyme(txt1, txt2):
    vowels = ('a', 'e', 'i', 'o', 'u')
    t1_vowel = sorted(c for c in list(txt1.lower().split()[-1]) if c in vowels)
    t2_vowel = sorted(c for c in list(txt2.lower().split()[-1]) if c in vowels)
    return t1_vowel == t2_vowel
