def checkio(data: str) -> bool:
    upper_count = 0
    lower_count = 0
    digit = 0
    length = len(data) >= 10
    for ch in data:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
        elif ch.isdigit():
            digit += 1
    pass_check = upper_count, lower_count, digit, length
    return all(pass_check)
