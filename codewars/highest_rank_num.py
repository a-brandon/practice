def highest_rank(arr: list) -> int:
    """
    Displays most frequent number in an array.
    
    Shows the most frequent number in an array. If there are two numbers
    that are the most frequent, the max number will be returned.
    
    Args:
        arr: List of integers.
    
    Returns:
        Max number from most frequent numbers.
    """
    freq = max({num: arr.count(num) for num in arr}.values())
    return max([num for num in arr if arr.count(num) == freq])
