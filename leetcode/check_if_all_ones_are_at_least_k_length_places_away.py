class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        one_locs = [i for i, n in enumerate(nums) if n == 1]
        return all(one_locs[i + 1] > one_locs[i] + k for i, _ in enumerate(one_locs[:-1]))