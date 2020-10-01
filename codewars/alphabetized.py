def alphabetized(s):
    return ''.join(sorted((ch for ch in s if ch.isalpha()), key=str.lower))