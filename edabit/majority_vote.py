def majority_vote(lst: list):
    """Finds majority vote.
    
    Finds the majority vote in a list. A majority vote is an element
    that occurs > N / 2 times in a list (where N is the length of the list.)
    
    Args:
        lst: List of votes
    
    Returns:
        The majority vote."""
    for el in lst:
        if lst.count(el) > len(lst) / 2:
            vote = el
            return vote
    return None
