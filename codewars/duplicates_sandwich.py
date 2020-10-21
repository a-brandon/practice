def duplicate_sandwich(arr):
    duplicates = []
    for i, n in enumerate(arr):
        if n in duplicates:
            return arr[arr.index(n) + 1:i]
        duplicates.append(n)