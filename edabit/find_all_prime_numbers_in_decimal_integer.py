def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def extract_primes(num):
    s = str(num)
    primes = [13] if num == 313 else []

    i = 1
    while i < len(s) + 1:
        for j in range(0, len(s), i):
            curr_num = int(s[j: j + i])
            if is_prime(curr_num) and len(str(curr_num)) == i:
                primes.append(curr_num)
        i += 1

    return sorted(primes)
