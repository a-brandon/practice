from string import ascii_lowercase


def in_alpha(word):
    word_list = [letter for letter in word if letter.isalpha()]
    temp_list = [i for ch in word_list for i, letter in enumerate(ascii_lowercase, start=1) if letter == ch]
    if sum(temp_list) % 2 == 0:
        return True
    return False
