import string


def get_hash_tags(txt):
    clean_string = ''.join(c for c in txt if c not in string.punctuation).split()
    if len(clean_string) < 3:
        return sorted(map(lambda s: f'#{s.lower()}', clean_string), key=len, reverse=True)
    max_len = len(max(clean_string, key=len))
    return sorted(map(lambda s: f'#{s.lower()}', clean_string), key=len, reverse=True)[0:3]
