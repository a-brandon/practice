def is_undulating(n: int) -> bool:
    """Checks if a given number is undulating.

    A number n is undulating when the following conditions are all true:

    n has at least three digits.
    n has exactly two different digits.
    The two digits of n are alternating without repeating groups.
    
    Args:
        n: An integer
    
    Returns:
        True or False
    """
    undul_check = [len(str(n)) >= 3, len(set(str(n))) == 2]
    for i in range(len(str(n)) - 2):
        if str(n)[i] != str(n)[i + 2]:
            return False
        else:
            undul_check.append(1)
    return all(undul_check)
