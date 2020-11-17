def solution(value):
    return f'Value is {"0" * (5 - len(str(value)))}{("{}" * len(str(value))).format(*str(value))}'