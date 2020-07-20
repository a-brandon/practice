class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        l = sorted(nums, reverse=True)
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

        for i, n in enumerate(nums):
            if n in l[0:3]:
                nums[i] = medals[l.index(n)]
            else:
                nums[i] = str(l.index(n) + 1)

        return nums