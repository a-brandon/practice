def abcmath(a, b, c):
    for i in range(b):
        a += a
    added_sum = a
    if added_sum % c == 0:
        return True
    return False
