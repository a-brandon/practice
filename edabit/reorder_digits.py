def reorder_digits(lst: list, direction: str) -> list:
    """Reorders digits.

    Based on the direction specified, reorders each digit in the list.

    Args:
        :param lst: A list of digits to be reordered.
        :param direction: The direction in which to reorder the elements in the list.

    Returns:
        A list of reordered elements.
    """
    if direction == 'asc':
        return [int(''.join(sorted(str(el)))) for el in lst]
    else:
        return [int(''.join(sorted(str(el), reverse=True))) for el in lst]
