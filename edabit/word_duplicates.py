def no_duplicate_letters(phrase):
    split_phrase = phrase.split()
    for word in split_phrase:
        for letter in word:
            if word.count(letter) == 2:
                return False
    return True
