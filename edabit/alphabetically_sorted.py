from string import punctuation


def is_alphabetically_sorted(sentence):
    # Needs a lot of refactoring. Bad bruteforce solution
    new_sentence = ''
    for ch in sentence:
        if ch not in punctuation:
            new_sentence += ch.lower()
    split_sentence = new_sentence.split()
    count = 0
    for chars in split_sentence:
        joined_word = [''.join(sorted(chars))]
        for word in joined_word:
            if word in split_sentence and len(word) >= 3:
                count += 1
    return bool(count)
