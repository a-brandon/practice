class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        max_diff = 0

        if len(nums) >= 2:
            arr = sorted(nums)

            for i, _ in enumerate(arr[:-1]):
                calc = arr[i + 1] - arr[i]
                if calc > max_diff:
                    max_diff = calc

        return max_diff