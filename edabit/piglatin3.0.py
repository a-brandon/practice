def find_vowel_index(word):
    for i, c in enumerate(word):
        if c in ('a', 'e', 'i', 'o', 'u'):
            return i


def pig_latin_sentence(sentence):
    words = sentence.split()
    for i, word in enumerate(words):
        if word[0] in ('a', 'e', 'i', 'o', 'u'):
            words[i] = word + 'way'
        else:
            vowel_idx = find_vowel_index(word)
            words[i] = word[vowel_idx:] + word[:vowel_idx] + 'ay'
    return ' '.join(words)
