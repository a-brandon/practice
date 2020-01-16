def cap_last(txt):
    split_words = txt.split()
    new_sentence = []
    for word in split_words:
        if word[-1].islower():
            last_letter = word[-1].upper()
            new_sentence.append(word[0:-1] + last_letter)
        else:
            return txt
    return ' '.join(new_sentence)
