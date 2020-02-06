def reverse_alternate(string: str) -> str:
    """
    Reverses every other word.
    
    Args:
        string: A string.
        
    Returns:
        A string with every other word reversed. 
        Punctuations are included with the word.
    """
    sep_string = string.strip().split()
    res = []
    for word in sep_string:
        if word in sep_string[1::2]:
            res.append(word[::-1])
        else:
            res.append(word)
    return ' '.join(res)
