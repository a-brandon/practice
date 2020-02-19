def find_squares(n: int) -> int:
    """R-1.6

    Write a short Python function that takes a positive integer
    n, and returns the sum of the squares of all the odd positive
    integers smaller than n."""
    squares = []
    for i in range(1, n):
        if i % 2 != 0:
            squares.append(i ** 2)
    return sum(squares)
