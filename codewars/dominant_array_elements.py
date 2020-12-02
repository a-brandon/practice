def solve(arr):
    return [n for i, n in enumerate(arr[0:-1]) if n > sorted(arr[i + 1:])[-1]] + [arr[-1]]