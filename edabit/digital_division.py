def check_exact_digits(n):
    return all(1 if not n % int(x) else 0 for x in str(n) if int(x))


def check_exact_sum(n):
    return True if n % sum((int(x) for x in str(n))) == 0 else False


def check_product(n):
    nums = (int(x) for x in str(n))
    prod = 1
    for x in nums:
        prod *= x
    return True if n % prod == 0 else False


def digital_division(n):
    if '0' in str(n):
        return sum([check_exact_digits(n), check_exact_sum(n)])
    elif all((check_exact_digits(n), check_exact_sum(n), check_product(n))):
        return 'Perfect'
    tests = sum([check_exact_digits(n), check_exact_sum(n), check_product(n)])
    return tests or 'Indivisible'
