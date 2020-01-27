def char_appears(sentence, char):
    split_sentence = sentence.lower().split()
    return [word.count(char) for word in split_sentence]
