def char_appears(sentence: str, char: str) -> list:
    split_sentence = sentence.lower().split()
    return [word.count(char) for word in split_sentence]
