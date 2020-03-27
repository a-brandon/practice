def is_decbin(n):
    if str(n) == str(n)[::-1]:
        f_bin = bin(n)[2:]
        r_bin = bin(n)[2:][::-1]
        if f_bin == r_bin:
            return True
    return False

def palindrome_type(n):
    if is_decbin(n):
        return 'Decimal and binary'
    elif bin(n)[2:] == bin(n)[2:][::-1]:
        return 'Binary only'
    elif str(n) == str(n)[::-1]:
        return 'Decimal only'
    return 'Neither'
