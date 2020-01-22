def steps_to_convert(txt: str) -> int:
    upper_count = len([letter for letter in txt if letter.isupper()])
    lower_count = len([letter for letter in txt if letter.islower()])
    if upper_count > lower_count:
        return lower_count
    return upper_count
