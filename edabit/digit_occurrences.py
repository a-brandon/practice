def digit_occurrences(start: int, end: int, digit: int):
    # This is very ugly
    numbers = [str(i) for i in range(start, end+1)]
    count = 0
    temp_list1 = []
    temp_list2 = []
    for n in numbers:
        if int(n) < 0:
            j = n.lstrip('-')
            for s in j:
                temp_list1.append(s)
        else:
            for d in n:
                temp_list2.append(d)
    for digits in temp_list1 + temp_list2:
        if int(digits) == digit:
            count += 1
    return count
