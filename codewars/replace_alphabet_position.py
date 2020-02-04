from string import ascii_lowercase


def alphabet_position(text):
    alphabet = {letter: i for i, letter in enumerate(ascii_lowercase, start=1)}
    return ' '.join([str(alphabet[letter]) for letter in text.lower() if letter.isalpha()])
