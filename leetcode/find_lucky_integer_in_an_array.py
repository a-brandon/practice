class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = []
        for n in set(arr):
            if arr.count(n) == n:
                nums.append(n)

        if nums:
            return max(nums)

        return -1