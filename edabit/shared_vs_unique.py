def letters(word1: str, word2: str) -> list:
    # Bad brute force 
    shared_letters = []
    unique_one = []
    unique_two = []
    for letter in word1:
        if letter in word2:
            shared_letters.append(letter)
    for letter in word1:
        if letter not in word2:
            unique_one.append(letter)
    for letter in word2:
        if letter not in word1:
            unique_two.append(letter)
    return [''.join(sorted(set(shared_letters)))] + [''.join(sorted(set(unique_one)))] + [''.join(sorted(set(unique_two)))]
