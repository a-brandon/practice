def censor_string(txt: str, lst: list, char: str)-> str:
    split_txt = txt.split()
    result = []
    for word in split_txt:
        if word in lst:
            result.append(len(word) * char)
        else:
            result.append(word)
    return ' '.join(result)
