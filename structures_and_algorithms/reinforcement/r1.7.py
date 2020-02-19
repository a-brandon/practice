def add_squares(n: int) -> int:
    """R-1.7

    Give a single command that computes the sum from
    Exercise R-1.6, relying on Python's comprehension syntax
    and the built-in sum function."""
    return sum(i ** 2 for i in range(n) if i % 2 != 0)
