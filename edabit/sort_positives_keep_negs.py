def pos_neg_sort(lst):
    positives = sorted(x for x in lst if x > 0)
    sorted_list = [positives.pop(0) if x > 0 else x for x in lst]
    return sorted_list or []
