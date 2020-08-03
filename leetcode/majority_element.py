class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {n: nums.count(n) for n in set(nums)}
        max_count = len(nums) / 2

        for k, v in counts.items():
            if v > max_count:
                return k