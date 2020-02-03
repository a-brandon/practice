def longest(s1, s2):
    """Take 2 strings s1 and s2 including only letters from a to z. 
    Return a new sorted string, the longest possible, containing distinct letters."""
    return ''.join(sorted(set(s1 + s2)))
