def percent_filled(box):
    temp_list = [list(el) for el in list(box)]
    temp_list_c = []
    for arr in temp_list:
        temp_list_c += arr
    flattened_list = [x for x in temp_list_c if x != '#']
    fills = flattened_list.count('o')
    total_spaces = flattened_list.count(' ') + fills
    percentage = fills / total_spaces * 100
    return f'{round(percentage)}%'
