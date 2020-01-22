def steps_to_convert(txt: str) -> int:
    upper_count = 0
    lower_count = 0
    for ch in txt:
        if ch.islower():
            lower_count += 1
        else:
            upper_count += 1
    if upper_count > lower_count:
        return lower_count
