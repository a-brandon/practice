def is_alternating(s: str) -> bool:
    """
    Checks if a string has alternating characters.
    
    Uses the enumerate function, and slices the string up
    to the second-to-last character, to prevent an index error on iteration.
    Iterates through the string, and checks if a character is equal to
    the character two index positions ahead of it.
    """
    for i, _ in enumerate(s[:-2]):
        if s[i] != s[i + 2]:
            return False
