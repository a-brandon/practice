def delete_nth(order,max_e):
    l = []
    for i in order:
        l.append(i)
        if l.count(i) > max_e:
            l = l[:-1]
    return l