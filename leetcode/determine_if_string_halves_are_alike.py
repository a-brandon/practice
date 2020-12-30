class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x = len(s) // 2
        l, r = s[0:x], s[x:]
        return sum(c in 'aeiouAEIOU' for c in l) == sum(c in 'aeiouAEIOU' for c in r)