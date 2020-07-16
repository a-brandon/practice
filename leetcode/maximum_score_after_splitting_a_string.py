class Solution:
    def maxScore(self, s: str) -> int:
        splits = 0

        for i in range(len(s)):
            z, o = s[0:i + 1], s[i + 1:]

            if z and o:
                total = z.count('0') + o.count('1')

                if total > splits:
                    splits = total

        return splits