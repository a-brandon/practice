class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_nums = set()

        for n in nums:
            if n in unique_nums:
                return n

            unique_nums.add(n)