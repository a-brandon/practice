def order_breaker(array):
    a = array[:]

    for i, n in enumerate(array):
        x = a.pop(i)
        if a == sorted(a):
            return x
        else:
            a = array[:]