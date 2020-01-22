def count_palindromes(num1, num2):
    count = 0
    result = [str(num) for num in range(num1, num2 + 1)]
    for digit in result:
        if digit == digit[::-1]:
            count += 1
    return count
