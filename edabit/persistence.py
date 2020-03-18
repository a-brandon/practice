def additive_persistence(n):
    iterations = 0
    while len(str(n)) > 1:
        n = sum(int(i) for i in str(n))
        iterations += 1
    return iterations

def multiplicative_persistence(n):
    iterations = 0
    n = str(n)
    prod = 1
    while len(n) > 1:
        nums = [int(i) for i in n]
        for num in nums:
            prod *= num
        n = str(prod)
        prod = 1
        iterations += 1
    return iterations
