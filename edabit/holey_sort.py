def holey_sort(lst):
    holes = {4: 1, 6: 1, 9: 1, 0: 1, 8: 2}
    return sorted(lst, key=lambda n: sum(holes.get(int(x), 0) for x in str(n)))


print(holey_sort([8, 121, 41, 66]))
