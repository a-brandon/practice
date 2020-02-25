def flip_list(arr):
    horizontal_arr = []
    if not arr:
        return arr
    elif type(arr[0]) == list:
        for elem in arr:
            horizontal_arr.append(elem[0])
    else:
        return [[elem] for elem in arr]
    return horizontal_arr
