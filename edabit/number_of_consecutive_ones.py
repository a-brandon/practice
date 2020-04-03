def count_ones(lst):
    l = ''.join(map(str, lst)).replace('0', ' ').split(' ')
    return sum(1 for el in l if '1' in el and len(el) >= 2)
