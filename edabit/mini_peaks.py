def mini_peaks(arr: list) -> list:
    if len(arr) == 3:
        return []
    result = []
    for i in range(len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            result.append(arr[i])
    return result
