class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s
        elif s.isalpha() or s.isdigit():
            return ''

        letters, nums = [], []

        for c in s:
            if c.isdigit():
                nums.append(c)
            else:
                letters.append(c)

        m = max(letters, nums, key=len)
        n = nums if m == letters else letters
        j = [l + r for l, r in zip(m, n)]

        if len(letters) != len(nums):
            j += m[-1]

        return ''.join(j)