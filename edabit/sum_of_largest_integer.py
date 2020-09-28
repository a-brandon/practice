def largest_digit_sum(n):
    digit_sums = {}

    while n > 0:
        digit_sums[n] = sum(int(i) for i in str(n))
        n -= 1

    return max(digit_sums, key=digit_sums.get)