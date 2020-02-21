"""C-1.22

Write a short Python program that takes two arrays a and b
of length n storing int values, and returns the dot product of a and b.
That is, it returns an array c of length n such that c[i] = a[i] * b[i]."""


def calculate_dot(a: list, b: list) -> list:
    return [a[i] * b[i] for i, _ in enumerate(a)]
