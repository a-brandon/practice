def show_the_love(lst):
    min_num = min(lst)
    total = sum(x * 0.25 for x in lst if x != min_num)
    l = [x - (x * 0.25) if x != min_num else x + total for x in lst]
    res = []
    for x in l:
        if str(x)[2:] == '.0':
            print(x)
            res.append(int(x))
        else:
            res.append(x)
    return res
