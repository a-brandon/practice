def has_identical(arr):
    row_sums = [sum(row) for row in arr]
    col_sums = [sum(col) for col in zip(*arr)]
    for num in row_sums:
        if num in col_sums:
            return True
    return False
