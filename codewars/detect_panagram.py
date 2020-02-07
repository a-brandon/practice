from string import ascii_lowercase


def is_pangram(s: str) -> bool:
    """
    Detects panagrams.

    Checks if every letter in the string contains a letter in the alphabet
    at least once.

    Args:
        s: A string.

    Returns:
        True or False.
    """
    count = 0
    for letter in s.lower():
        if letter in ascii_lowercase:
            count += 1
            if count == len(ascii_lowercase):
                return True
    return False

