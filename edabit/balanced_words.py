from string import ascii_lowercase


def balanced_word(word):
    if word == word[::-1]:
        return True
    vals = {letter: i for i, letter in enumerate(ascii_lowercase, start=1)}
    if len(word) % 2 == 0:
        first_half = sum([vals[c] for c in list(word[:len(word) // 2])])
        second_half = sum([vals[c] for c in list(word[len(word) // 2:])])
        if first_half == second_half:
            return True
    odd_first = sum([vals[c] for c in list(word[:len(word) // 2])])
    odd_second = sum([vals[c] for c in list(word[len(word) // 2:][1:])])
    return True if odd_first == odd_second else False
