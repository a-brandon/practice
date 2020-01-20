def match_last_item(lst: list) -> bool:
    string_list = ''.join([str(i) for i in lst[0:-1]])
    return string_list == lst[-1]
