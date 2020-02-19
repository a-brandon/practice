def pos_neg_sort(arr):
    positives = sorted(i for i in arr if i > 0)
    res = []
    for num in arr:
        if num < 0:
            res.append(num)
        else:
            elem = positives.pop(0)
            res.append(elem)
    return res
