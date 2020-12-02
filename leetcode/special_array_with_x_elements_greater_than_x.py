class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 1

        while x < len(nums) + 1:
            numbers = [i for i in nums if i >= x]

            if len(numbers) == x:
                return x

            x += 1

        return -1