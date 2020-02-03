def find_it(seq: list) -> int:
    """Find integer that appears an odd number of times."""
    freq = {n: seq.count(n) for n in seq}
    for k, v in freq.items():
        if v % 2 != 0:
            return k
