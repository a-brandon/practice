def triple_double(num1, num2):
    x, y = str(num1), str(num2)
    for i in x:
        if str(i) * 3 in x and str(i) * 2 in y:
            return 1
    return 0