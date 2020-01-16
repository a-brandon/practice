from collections import Counter

def return_unique(lst):
    c = Counter(lst)
    unique_list = []
    for k, v in c.items():
        if v == 1:
            unique_list.append(k)
    return unique_list
