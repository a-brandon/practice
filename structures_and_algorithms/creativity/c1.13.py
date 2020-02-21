"""C-1.13

Write a pseudo-code description of a function that reverses
a list of n integers, so that the numbers are listed in the opposite
order than they were before, and compare this method to an equivalent
Python function for doing the same thing."""


# Create a function called reverse_nums(nums: list) -> list
# The parameter is gonna be a list of numbers
# The return value is gonna be a list
# Return the numbers sliced in reversed order: [::-1]


def reverse_nums(nums: list) -> list:
    return nums[::-1]


# Function to compare: reversed()
# reversed() returns an iterator that accesses a sequence in reverse order
num_list = [1, 2, 3]
reversed_nums = list(reversed(num_list))
