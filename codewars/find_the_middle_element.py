def gimme(input_array):
    arr = sorted(input_array)
    return input_array.index(arr[len(arr) // 2])