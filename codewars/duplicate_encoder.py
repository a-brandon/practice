def duplicate_encode(word: str) -> str:
    """
    Encodes a string.
    
    If the count of a character in the string is equal to 1,
    '(' will replace the character in a new string, otherwise ')' will replace
    the character in a new string.
    
    Args:
        word: A string.
    
    Returns:
        A string with it's characters replaced by '(', or ')'
        
    """
    cased = word.lower()
    output = ''
    for ch in cased:
        if cased.count(ch) == 1:
            output += '('
        elif cased.count(ch) > 1:
            output += ')'
    return output
