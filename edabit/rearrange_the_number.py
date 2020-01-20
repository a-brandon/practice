def rearranged_difference(num):
    min_list = sorted(i for i in str(num))
    min_number = int(''.join([i for i in min_list]))
    max_list = list(reversed(min_list))
    max_number = int(''.join(max_list))
    return max_number - min_number
