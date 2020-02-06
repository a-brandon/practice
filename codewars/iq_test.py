def iq_test(numbers: str) -> int:
    """Finds odd number out.

    In a group of numbers, if every number but one is odd,
    it'll return the odd number. Vice-versa for even numbers.

    Args:
        numbers: A string of numbers

    Returns:
        The odd or even number out."""
    num_cast = list(map(int, numbers.split(' ')))
    evens = [i for i in num_cast if i % 2 == 0]
    odds = [i for i in num_cast if i % 2 != 0]
    if len(evens) > len(odds):
        for i, num in enumerate(num_cast, start=1):
            if num == odds[0]:
                return i
    else:
        for i, num in enumerate(num_cast, start=1):
            if num == evens[0]:
                return i
