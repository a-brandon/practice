class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = 0

        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j:
                    continue
                else:
                    res = (nums[i] - 1) * (nums[j] - 1)
                    if res > max_val:
                        max_val = res

        return max_val