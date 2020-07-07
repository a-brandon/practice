class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        pairs = [nums[i: i + 2] for i in range(0, len(nums), 2)]
        res = []
        for i, (f, v) in enumerate(pairs):
            res += [v] * f
        return res