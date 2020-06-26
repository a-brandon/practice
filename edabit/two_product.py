def two_product2(arr, n):
    """O(N) time complexity solution.
    Curious as to why this solution doesn't pass tests. First pair found was [72, 2600]?"""
    i, j = 0, 0
    while i < len(arr) - 1:
        if j == len(arr):
            i += 1
            j = 0
        curr_num, prod_num = arr[i], arr[j]
        if prod_num == curr_num:
            j += 1
            continue
        if curr_num * prod_num == n:
            return [curr_num, prod_num]
        j += 1