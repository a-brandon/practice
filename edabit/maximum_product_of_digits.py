def create_num_dict(n):
    numbers = {}
    for i in range(0, n + 1):
        if '0' not in str(i):
            x = 1
            digits = [int(n) for n in str(i)]
            for num in digits:
                x *= num
            numbers[i] = x
    return numbers


def max_product(n):
    numbers = create_num_dict(n)
    max_val = max(numbers.values())
    max_prods = [k for k, v in numbers.items() if v == max_val]
    return max_prods

