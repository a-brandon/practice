def sum_of_holes(N: int) -> int:
    holes = {0: 1, 4: 1, 6: 1, 8: 2, 9: 1}
    total = []
    for num in range(1, N + 1):
        arr = list(str(num))
        for x in arr:
            if int(x) in holes:
                total.append(holes[int(x)])
    return sum(total)
