class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if all(x == 0 for x in nums):
            return 0
        ones = ''
        for x in nums:
            if x == 1:
                ones += str(x)
            else:
                ones += ' '
        return len(max(ones.split()))
