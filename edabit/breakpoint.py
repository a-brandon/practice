def break_point(num):
    l = list(map(int, str(num)))
    for i in range(len(l)):
        left, right = l[0:i + 1], l[i + 1:]
        if sum(left) == sum(right):
            return True
    return False
