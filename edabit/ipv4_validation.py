def is_valid(txt):
    valid = 0
    ip = txt.split('.')

    for d in ip:
        if not d.isdigit():
            return False
        elif d == '0':
            valid += 1
        elif all(('0' not in str(d)[:-1],
                  not d.startswith('.'), 1 <= int(d) <= 255)):
            valid += 1

    return valid == 4