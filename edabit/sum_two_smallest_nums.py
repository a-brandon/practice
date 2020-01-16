def sum_two_smallest_nums(lst):
    positive_list = sorted(number for number in lst if number > 0)
    return sum(positive_list[0:2])
