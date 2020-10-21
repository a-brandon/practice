def remove_bmw(string):
    if not isinstance(string, str):
        return 'This program only works for text'
    return string.translate(str.maketrans('bBmMwW', ' ' * 6)).replace(' ', '')