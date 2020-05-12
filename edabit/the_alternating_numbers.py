def is_alternating(num):
    if num <= 0:
        return False

    alts = {1: 0, 0: 1}
    n = str(num)
    digits = [n[0]]
    for x in n[1:]:
        prev_rem, curr_rem = int(digits[-1]) % 2, int(x) % 2
        if alts[curr_rem] == prev_rem:
            digits.append(x)
						
    return int(''.join(digits)) == num
