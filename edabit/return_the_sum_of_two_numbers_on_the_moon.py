def lunar_sum(number1, number2):
    n1, n2 = list(str(number1)), list(str(number2))
    if len(n1) > len(n2):
        diff = len(n1) - len(n2)
        for i in range(diff):
            n2.insert(0, '0')
    elif len(n2) > len(n1):
        diff = len(n2) - len(n1)
        for i in range(diff):
            n1.insert(0, '0')
    return int(''.join(x if x > y else y for x, y in zip(n1, n2)))
