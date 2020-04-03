def count_ones(lst):
    nums = ''.join(map(str, lst)).replace('0', ' ').split(' ')
    return sum(1 for el in nums if '1' in el and len(el) >= 2)
