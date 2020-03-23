factors = []
for i in range(2, 13195):
    if 13195 % i == 0 and is_prime(i):
        factors.append(i)
largest_prime = max(factors)
