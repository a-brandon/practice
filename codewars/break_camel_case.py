def solution(s):
    broken_case = ''
    for c in s:
        if c.islower():
            broken_case += c
        else:
            broken_case += ' '
            broken_case += c
    return broken_case
