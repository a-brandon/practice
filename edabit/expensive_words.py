from string import punctuation, ascii_lowercase


def get_sentence_value(sentence):
    s = ''.join(c for c in sentence if c not in punctuation).split()
    total = 0

    for word in s:
        vals = sum(ascii_lowercase.index(c.lower()) + 1 for c in list(word))
        if word.isupper():
            total += vals * 2
        else:
            total += vals

    return total
