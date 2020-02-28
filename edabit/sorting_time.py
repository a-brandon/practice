def sort_array(arr):
    sorted_arr = []
    while arr:
        min_num = min(arr)
        sorted_arr.append(min_num)
        arr.remove(min_num)
    return sorted_arr
