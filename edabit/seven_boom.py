def seven_boom(lst):
    str_list = [str(num) for num in lst]
    boom_list = [int(digit) for num in str_list for digit in num if int(digit) == 7]
    if boom_list:
        return 'Boom!'
    return 'there is no 7 in the list'
