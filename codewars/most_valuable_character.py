def solve(st):
    lookup = {c: st.rindex(c) - st.index(c) for c in set(st)}
    return sorted(ch for ch in lookup if lookup[ch] == max(lookup.values()))[0]