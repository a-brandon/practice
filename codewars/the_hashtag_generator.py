def generate_hashtag(s):
    words = f"#{''.join(w.capitalize() for w in s.split())}"
    if not words or not s:
        return False
    return False if len(words) > 140 else words