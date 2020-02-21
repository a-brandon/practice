def find_unique(nums: list) -> bool:
    """C1-15

    Write a Python function that takes a sequence
    of numbers and determines if all the numbers are
    different from each other (that is, they are distinct)."""
    return sorted(set(nums)) == sorted(nums)
