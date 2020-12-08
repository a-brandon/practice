class Solution:
    def customSortString(self, S: str, T: str) -> str:
        incl, excl = [], []

        for c in T:
            incl.append(c) if c in S else excl.append(c)

        return ''.join(sorted(incl, key=S.index) + excl)