def sum_digits(a: int, b: int) -> int:
    str_cast = (str(i) for i in range(a, b + 1))
    result = []
    for num in str_cast:
        for digit in num:
            result.append(int(digit))
    return sum(result)
