class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        letter_count = {(s.index(c), s.rindex(c)): s.count(c) for c in set(s)}

        if all(v <= 1 for v in letter_count.values()):
            return -1

        max_sub = 0

        for x, y in letter_count:
            sub_str = len(s[x: y][1:])
            max_sub = sub_str if sub_str > max_sub else max_sub

        return max_sub