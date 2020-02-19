def add_squares(n: int) -> int:
    """R-1.4

    Write a short Python function that takes a positive
    integer n, and returns the sum of the squares of all
    the positive integers smaller than n."""
    squares = []
    for i in range(n):
        squares.append(i ** 2)
    return sum(squares)
