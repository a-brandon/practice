def validate_spelling(txt: str) -> bool:
    words = txt.split()
    comp_word = words[-1][:-1]
    words = ''.join(words[:-1]).replace('.', '').title()
    return comp_word == words
