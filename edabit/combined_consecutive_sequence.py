def consecutive_combo(lst1, lst2):
    temp = []
    ordered_list = sorted(lst1 + lst2)
    for i in range(len(ordered_list) - 1):
        if ordered_list[i + 1] == ordered_list[i] + 1:
            temp.append(i)
        else:
            return False
    return True
