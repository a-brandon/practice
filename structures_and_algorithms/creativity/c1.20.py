from random import randint, shuffle

"""C-1.20

Python's random module includes a function that shuffles(data)
that accepts a list of elements and randomly reorders the elements
so that each possible order occurs with equal probability. The random
module includes a more basic function randint(a, b) that returns
a uniformly random integer from a to b (including both endpoints).
Using only the randint function, implement your own version of the shuffle
function."""


def rand_shuffle(nums: list) -> list:
    shuffled_seq = []
    while len(shuffled_seq) < len(nums):
        num = randint(nums[0], nums[-1])
        shuffled_seq.append(num)
    return shuffled_seq
