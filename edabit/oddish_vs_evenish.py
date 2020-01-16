def oddish_or_evenish(num):
    sum_of_nums = sum([int(number) for number in str(num)])
    if sum_of_nums % 2 == 0:
        return 'Evenish'
    return 'Oddish'
