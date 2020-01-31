def checkio(text: str) -> str:
    cased_text = text.lower()
    result = []
    freq = {ch: cased_text.count(ch) for ch in cased_text if ch.isalpha()}
    max_count = max(freq.values())
    for k, v in freq.items():
        if v == max_count:
            result.append(k)
    return sorted(result)[0]
