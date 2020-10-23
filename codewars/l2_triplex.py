def triple_x(s):
    if 'x' not in s:
        return False
    first_inst = s.index('x')
    return s[first_inst:first_inst + 3] == 'xxx'