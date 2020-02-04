def delete_nth(order, max_e):
    """
    Parameters:
    arg1 (list): List of numbers
    arg2 (int): Threshold for numbers in list

    Returns:
        A list of numbers less than max_e.
    """
    res = []
    for num in order:
        if res.count(num) < max_e:
            res.append(num)
    return res
