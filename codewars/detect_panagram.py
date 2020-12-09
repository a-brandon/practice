import string


def is_pangram(s):
    return all(c in s.lower() for c in string.ascii_lowercase)