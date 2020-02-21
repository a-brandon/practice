def create_comp():
    """C-1.18

    Demonstrate how to use Python's list comprehension
    to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72]."""
    return [i * (i + 1) for i in range(9)]
