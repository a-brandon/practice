def balance(left: str, right: str) -> str:
    """
    Checks which string is heavier: left or right.
    
    Exclamation marks are worth two points, question marks are worth three points.
    Counts up how many times exclamation marks and question marks appear in the left and right strings.
    Determines which side is heavier based on the count. If the counts are equal, returns 'Balance'.
    
    Args:
        left: A string of exclamation and question marks.
        right: A string of exclamation and question marks.
    
    Returns:
        "Left", "Heavy", or "Balance" depending on the count.
    """
    left_marks = left.count('!') * 2 + left.count('?') * 3
    right_marks = right.count('!') * 2 + right.count('?') * 3
    if left_marks > right_marks:
        return 'Left'
    elif right_marks > left_marks:
        return 'Right'
    return 'Balance'
