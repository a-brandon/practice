from string import ascii_lowercase, punctuation


def get_sentence_value(txt):
    score = {c: i for i, c in enumerate(ascii_lowercase, start=1)}
    txt = ''.join([c for c in txt if c not in punctuation]).split()
    value = 0
    for word in txt:
        if word.islower():
            div = list(word)
            nums = sum([score[letter] for letter in div])
            value += nums
        elif word.isupper():
            div = list(word)
            nums = sum([score[letter.lower()] for letter in div])
            value += nums * 2
        else:
            div = list(word)
            nums = sum([score[letter.lower()] for letter in div])
            value += nums
    return value
