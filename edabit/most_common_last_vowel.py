from string import punctuation


def common_last_vowel(txt):
    txt = ''.join([c for c in txt if c not in punctuation]).lower().split()
    vowels = []
    for word in txt:
        if word[-1] not in ['a', 'e', 'i', 'o', 'u']:
            for letter in word:
                if letter in ['a', 'e', 'i', 'o', 'u']:
                    vowels.append(letter)
        elif word[-1] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(word[-1])
    return max(vowels)
