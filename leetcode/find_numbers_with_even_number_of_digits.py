class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0

        for n in nums:
            if not len(str(n)) % 2:
                counter += 1

        return counter