class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_total = sum(int(x) for x in str(n))
        nums = {i: [] for i in range(1, max_total + 1)}

        for i in range(1, n + 1):
            total = sum(int(x) for x in str(i))
            if total not in nums:
                nums[total] = [i]
            else:
                nums[total].append(i)

        largest_size = len(max(nums.values(), key=len))

        return sum(len(g) == largest_size for g in nums.values())