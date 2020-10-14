def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return f'{max(nums)} {min(nums)}'