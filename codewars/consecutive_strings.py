def longest_consec(strarr, k):
    if not strarr or 0 >= k or k > len(strarr):
        return ''

    consec_str = ''
    i = 0
    while i < len(strarr):
        sub = ''.join(strarr[i:k + i])

        if len(sub) > len(consec_str):
            consec_str = sub

        i += 1
    return consec_str