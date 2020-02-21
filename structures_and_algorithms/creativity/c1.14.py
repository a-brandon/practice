def find_distinct(nums: list) -> list:
    """C-1.14

    Write a short Python function that takes a sequence
    of integers values and determines if there is a distinct
    pair of numbers in the sequence whose product is odd"""
    odd_prods = []
    for i in nums:
        for j in nums:
            if i * j % 2 != 0:
                odd_prods.append([i, j])
    return odd_prods
