def sort_by_length(txt):
    return ' '.join(sorted(sorted(txt.split(), key=str.lower), key=len))