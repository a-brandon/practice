def count_ones(lst):
    ones = ''.join(map(str, lst)).split('0')
    return sum(1 for x in ones if len(x) >= 2)
