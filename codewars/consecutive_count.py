def get_consective_items(items, key):
    s, val = str(items), str(key)
    for ch in set(s):
        if ch != val:
            s = s.replace(ch, ' ')
    return len(max(s.split(), key=len))
