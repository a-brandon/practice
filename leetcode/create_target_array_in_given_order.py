class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_arr = []
        for i, n in zip(index, nums):
            target_arr.insert(i, n)
        return target_arr