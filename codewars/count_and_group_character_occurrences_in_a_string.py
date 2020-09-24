def get_char_count(s):
    txt = s.lower()
    counts = {ch: txt.count(ch) for ch in set(txt) if ch.isalpha() or ch.isdigit()}
    out = {x: [] for x in sorted(counts.values(), reverse=True)}

    for k, v in counts.items():
        if v in out:
            out[v].append(k)
            out[v].sort()

    return out