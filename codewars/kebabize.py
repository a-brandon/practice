def kebabize(sentence: str) -> str:
    """
    Kebabizes a string.

    Turns a camel-cased string into a kebab-cased string.
    
    Args:
        sentence: A camel-cased string.
    
    Returns:
        A kebab-cased string.
    """
    output = ''
    for ch in sentence:
        if ch.isupper():
            output += "-" + ch
        elif not ch.isdigit():
            output += ch
    return output.lower().strip('-')
