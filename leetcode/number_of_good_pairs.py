class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0

        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if nums[i] == nums[j] and i < j:
                    pairs += 1

        return pairs