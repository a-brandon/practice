class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([integers for integers in map(str, nums) if len(integers) % 2 == 0])
