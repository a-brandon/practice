def find_squares(n: int) -> int:
    """R-1.5

    Give a single command that commutes the sum
    from Exercise R-1.4, relying on Python's comprehension syntax,
    and the built-in sum function."""
    return sum(i ** 2 for i in range(1, n))
