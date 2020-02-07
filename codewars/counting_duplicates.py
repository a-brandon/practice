def duplicate_count(text: str) -> int:
    """
    Returns the count of distinct case-insensitive characters.

     Return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once 
     in the input string. 
     
     Args:
         text: A string
    
    Returns:
        The count of distinct case-insensitive characters.
    """
    cased = text.lower()
    freq = {c: cased.count(c) for c in cased}
    res = []
    for k, v in freq.items():
        if v >= 2:
            res.append(k)
    return len(res)
