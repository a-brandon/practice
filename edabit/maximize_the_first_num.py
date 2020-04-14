def max_possible(n1, n2):
    first_num = list(map(int, str(n1)))
    second_num = sorted(map(int, str(n2)), reverse=True)
    for i, x in enumerate(first_num):
        for j, y in enumerate(second_num):
            if y > x:
                first_num[i] = second_num[j]
                second_num.remove(y)
                break
    return int(''.join(map(str, first_num)))
