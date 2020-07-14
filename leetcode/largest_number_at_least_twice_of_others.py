class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest_num = max(nums)
        for x in nums:
            if x * 2 > largest_num and x != largest_num:
                return -1
        return nums.index(largest_num)