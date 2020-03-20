def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def find_harshad(num):
    digits = sum(int(i) for i in str(num))
    if num % digits == 0:
        return 'H'
    return 'Neither'


def moran(n):
    digits = sum(int(i) for i in str(n))
    if n % digits == 0 and is_prime(n // digits):
        return 'M'
    else:
        return find_harshad(n)
