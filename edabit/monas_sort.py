def number_of_swaps(arr: list) -> int:
    swaps = 0
    ordered = sorted(arr)
    while arr != ordered:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
    return swaps
