def sort_array(source_array):
    """You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places."""
    odds = sorted(i for i in source_array if i % 2 != 0)
    res = []
    for num in source_array:
        if num % 2 != 0:
            res.append(odds[0])
            del odds[0]
        else:
            res.append(num)
    return res
