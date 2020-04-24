def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_prime(num:int) -> int:
    if is_prime(num):
        return num

    while True:
        num += 1
        if is_prime(num):
            return num
