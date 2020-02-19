def add_squares(n: int) -> int:
    """R-1.5

    Give a single command that computes the sum
    from Exercise R-1.4,relying on Python's comprehension
    syntax and the built-in function sum"""
    return sum(i ** 2 for i in range(n))
