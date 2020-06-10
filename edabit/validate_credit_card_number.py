def validate_card(num):
    s = str(num)

    if not 14 <= len(s) <= 19:
        return False

    check_digit, rev_num = int(s[-1]), s[:-1][::-1]
    doubles = []

    for i, n in enumerate(rev_num, start=1):
        if i % 2:
            total = int(n) * 2
            if len(str(total)) > 1:
                total = sum(map(int, str(total)))
                doubles.append(total)
            else:
                doubles.append(total)
        else:
            doubles.append(int(n))

    final_sum = 10 - int(str(sum(doubles))[-1])
    return final_sum == check_digit


print(validate_card(1234567890123452))
