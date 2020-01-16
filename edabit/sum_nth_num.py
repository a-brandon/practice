def sum_every_nth(numbers, n):
    return sum([digit for digit in numbers[n-1::n]])
