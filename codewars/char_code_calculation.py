def calc(x):
    total_one = ''.join(str(ord(c)) for c in x)
    total_two = sum(list(map(int, total_one.replace('7', '1'))))
    return sum(map(int, total_one)) - total_two