from string import ascii_lowercase


def is_pangram(txt):
    return 'Pangram' if all(c in txt for c in ascii_lowercase) else False


def is_heterogram(txt):
    return 'Heterogram' if sorted(set(txt)) == sorted(txt) else False


def is_tautogram(sentence):
    return 'Tautogram' if all(c[0] == sentence[0][0] for c in sentence[1:]) else False


def is_transgram(sentence):
    letters = [c for c in sentence[0]]
    for word in sentence[1:]:
        if not any(c in letters for c in word):
            return False
    return 'Transgram'


def constraint(txt):
    letters = [c for c in txt.lower() if c.isalpha()]
    words = txt.lower().split()
    return (is_pangram(letters) or is_heterogram(letters)
            or is_tautogram(words) or is_transgram(words) or 'Sentence')
