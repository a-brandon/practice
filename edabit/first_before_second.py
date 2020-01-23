def first_before_second(s, first, second):
    first_count = s.count(first)
    result = ''
    for letter in s:
        if letter == first:
            result += letter
        elif letter == second:
            break
    return len(result) == first_count
