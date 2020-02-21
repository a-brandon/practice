def create_alphabet():
    """C-1.19

    Demonstrate how to use Python's list comprehension
    to produce the list ['a', 'b', 'c', ......, 'z'],
    but without having to type all 26 characters literally."""
    return [chr(i) for i in range(ord('a'), ord('z') + 1)]
