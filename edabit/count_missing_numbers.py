def count_missing_nums(arr):
    count = 0
    clean_arr = sorted(int(c) for c in arr if c.isdigit())
    for i in range(clean_arr[0], clean_arr[-1] + 1):
        if i not in clean_arr:
            count += 1
    return count
