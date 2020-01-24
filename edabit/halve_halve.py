def halve_count(a, b):
    result = []
    while a > b:
        a /= 2
        result.append(a)
    return len(result[0:-1])
