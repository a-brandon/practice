def factorial(n):
    result = [i for i in range(1, n+1)]
    prod = 1
    for num in result:
        prod *= num
    return prod
