def is_repdigit(num: int) -> bool:
    """Checks for repdigits.

    A repdigit is a positive number composed out of the same digit.
    
    Args:
        num: A number to check for being a repdigit.
    
    Returns:
        True or False.
    """
    if str(num)[0] == '-':
        return False
    return True if len(set(list(str(num)))) == 1 else False
