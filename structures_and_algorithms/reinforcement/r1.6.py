def add_squares(n: int) -> int:
    """R-1.6

    Write a short Python function that takes a positive
    integer n and returns the sum of the squares of the all
    the odd positive integers smaller than n."""
    squares = []
    for i in range(n):
        if i % 2 != 0:
            squares.append(i ** 2)
    return sum(squares)
