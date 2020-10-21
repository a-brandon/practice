def string_task(s):
    letters = [c.lower() if c not in 'AOYEUI' and c.isupper() else c for c in s if c.upper() not in 'AOYEUI']
    return ('.{}' * len(letters)).format(*letters)