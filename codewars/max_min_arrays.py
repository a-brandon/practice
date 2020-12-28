def solve(arr):
    sorted_arr = sorted(arr)
    result = []

    while len(sorted_arr) > 1:
        result.append(sorted_arr.pop())
        sorted_arr = sorted_arr[::-1]

    return result + sorted_arr
