def is_even(k: int) -> bool:
    """R-1.2

    Write a short Python function, is_even(k),
    that takes an integer value and returns True
    if k is even, and False otherwise. However,
    your function cannot use the multiplication,
    modulo, or division operators."""
    while k > 0:
        k -= 2
    return False if k < 0 else True
